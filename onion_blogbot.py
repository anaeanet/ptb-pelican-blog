from telegram import (InlineKeyboardButton, InlineKeyboardMarkup)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler)

from domain.model import User, UserState
from infrastructure.repositories import UserRepository
from infrastructure.factories import UserFactory
from infrastructure.persistence import SQLUserPersistence

import config

# Enable logging
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

__author__ = "anaeanet"


def init(conversation_handler, authorized_users, user_repo, bot, update, user_data=None):

    user = User(update.effective_user.id, update.effective_user.first_name)

    if user.user_id not in user_data:
        user_data[user.user_id] = user_repo

    # initialize authorized user if not already done earlier
    if user.user_id in authorized_users and not user_data[user.user_id].get_user_by_id(user.user_id):
        if user_data[user.user_id].save_user(user):
            logger.info("Initialized user %s (%s) due to first update being received: %s"
                        % (user.user_name, user.user_id, update))
        else:
            logger.warning("Initialized of user %s (%s) failed! User could not be authorized."
                           % (user.user_name, user.user_id))

    # default: end conversation if user not authorized
    next_state = ConversationHandler.END

    # restore previous user data
    user = user_data[user.user_id].get_user_by_id(user.user_id)

    if user is None:
        logger.info("Unauthorized user %s (%s) sent update %s" % (user.first_name, user.id, update))
    else:

        # user has an ongoing conversation -> reload and continue
        if user.user_state is not None:
            handlers = conversation_handler.states[user.user_state] + conversation_handler.fallbacks
            for h in handlers:
                if h.check_update(update):
                    logger.info("Restored user %s (%s) from state %s" % (user.user_name, user.user_id, user.user_state))
                    next_state = h.callback(bot, update, user_data=user_data)
                    break

        # no previous conversation was restored -> start a new one
        if next_state == ConversationHandler.END:

            if user.user_state is not None:
                logger.warning("Attempt to restore user %s (%s) failed! " % (user.user_state, user.user_id)
                               + "No matching callback function found for state %s." % user.user_state)

            logger.info("Starting new conversation with user %s (%s)" % (user.user_name, user.user_id))
            next_state = start(bot, update, user_data=user_data)

    return next_state


def start(bot, update, user_data=None):
    bot.send_message(update.effective_chat.id,
                     'Welcome to your mobile blogging bot!\r\n\r\n'
                     + 'I am here to help you create new blog posts or manage existing ones. '
                     + 'Just follow the interactive menu!')
    return main_menu(bot, update, user_data=user_data)


def main_menu(bot, update, user_data=None):
    user_repo = user_data[update.effective_user.id]
    user = user_repo.get_user_by_id(update.effective_user.id)

    # TODO write userrepository.update_user(user_id, **update_values)
    if user:
        user.user_state = UserState.MAIN_MENU
        user_repo.save_user(user)
        user = user_repo.get_user_by_id(update.effective_user.id)

    keyboard = [
        [InlineKeyboardButton("CREATE a draft", callback_data='/createdraft')]
    ]
    bot.send_message(update.effective_chat.id,
                     'What do you want to do?',
                     reply_markup=InlineKeyboardMarkup(keyboard))

    return ConversationHandler.END if user is None else user.user_state


def main_menu_callback(bot, update, user_data=None):
    data = update.callback_query.data

    if data == "/createdraft":
        next_state = None   # TODO
    elif data == "/updatedraft":
        next_state = None   # TODO
    elif data == "/deletedraft":
        next_state = None   # TODO
    elif data == "/updatepost":
        next_state = None   # TODO
    elif data == "/deletepost":
        next_state = None   # TODO
    else:
        next_state = None   # TODO get current state of user

    # TODO set user_state to next_state

    # TODO return user_state
    return next_state


def idle(bot, update, user_data=None):
    user = user_data[update.effective_user.id].get_user_by_id(update.effective_user.id)
    bot.send_message(update.message.chat.id, update.message.text)
    return ConversationHandler.END if user is None else user.user_state


def handle_error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))


def main():
    token = config.TOKEN
    authorized_users = config.AUTHORIZED_USERS
    database = config.DATABASE

    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    users = UserRepository(SQLUserPersistence(database), UserFactory())

    # Add conversation handler with the corresponding states
    conversation_handler = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.all,
                           lambda bot, update, user_data: init(conversation_handler,
                                                               authorized_users, users,
                                                               bot, update, user_data),
                           pass_user_data=True)],

        states={
            UserState.MAIN_MENU: [CallbackQueryHandler(main_menu_callback, pass_user_data=True)]
        },

        fallbacks=[
            CommandHandler('start', start, pass_user_data=True),
            MessageHandler(Filters.all, idle, pass_user_data=True)
        ]
    )
    dp.add_handler(conversation_handler)

    # log all errors
    dp.add_error_handler(handle_error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
