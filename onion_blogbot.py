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


def init(conversation_handler, authorized_users, repo, bot, update, user_data=None):
    user = update.effective_user
    next_state = ConversationHandler.END

    if not user_data:
        user_data = repo

    # initialize authorized user if not already done earlier
    if user.id in authorized_users and not user_data.get_user_by_id(user.id):
        if user_data.save_user(User(user.id, user.first_name, UserState.INIT)):     # TODO factory
            logger.info("Initialized user %s (%s) due to first update being received: %s"
                        % (user.first_name, user.id, update))

    # restore previous user data
    bot_user = user_data.get_user_by_id(user.id)
    if bot_user is not None:

        # user has just been initialized as authorized user, call start
        if bot_user.user_state is UserState.INIT:
            logger.info("Starting new conversation with user %s (%s)" % (user.first_name, user.id))
            next_state = start(bot, update, user_data=user_data)
        # user has been interacting with bot earlier and may have any state -> reload
        else:
            handlers = conversation_handler.states[bot_user.user_state] + conversation_handler.fallbacks
            for h in handlers:
                if h.check_update(update):
                    logger.info("Restored user %s (%s) from state %s" % (user.first_name, user.id, bot_user.user_state))
                    next_state = h.callback(bot, update, user_data=user_data)

            if next_state == ConversationHandler.END:
                logger.warning("Attempt to restore user %s (%s) failed. " % (user.first_name, user.id)
                               + "No matching callback function found for state %s. " % bot_user.state
                               + "Defaulting to state %s!" % UserState.INIT)
                next_state = start(bot, update, user_data=user_data)

    else:
        logger.info("Unauthorized user %s (%s) sent update %s" % (user.first_name, user.id, update))

    return next_state


def start(bot, update, user_data=None):
    bot.send_message(update.effective_chat.id
                     ,'Welcome to your mobile blogging bot!\r\n\r\n'
                     + 'I am here to help you create new blog posts or manage existing ones. '
                     + 'Just follow the interactive menu!')
    return main_menu(bot, update, user_data=user_data)


def main_menu(bot, update, user_data=None):
    keyboard = [
        [InlineKeyboardButton("CREATE a draft", callback_data='/createdraft')]
    ]
    bot.send_message(update.effective_chat.id
                     , 'What do you want to do?'
                     , reply_markup=InlineKeyboardMarkup(keyboard))
    return UserState.MAIN_MENU


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
        next_state = None

    return next_state


def idle(bot, update, user_data=None):
    bot.send_message(update.message.chat.id, update.message.text)
    return None


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))


def main():
    token = config.TOKEN
    authorized_users = config.AUTHORIZED_USERS
    database = config.DATABASE
    # TODO read other data from config

    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    repo = UserRepository(SQLUserPersistence(database), UserFactory())

    # Add conversation handler with the corresponding states
    conversation_handler = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.all
                           , lambda bot, update, user_data: init(conversation_handler
                                                                 , authorized_users
                                                                 , repo
                                                                 , bot, update, user_data)
                           , pass_user_data=True)],

        states={
            UserState.MAIN_MENU: [CallbackQueryHandler(main_menu_callback, pass_user_data=True)]
        },

        fallbacks=[
            CommandHandler('start', start, pass_user_data=True)
            , MessageHandler(Filters.all, idle, pass_user_data=True)],

        allow_reentry=False
    )
    dp.add_handler(conversation_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
