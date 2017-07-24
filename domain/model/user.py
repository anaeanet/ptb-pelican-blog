from domain.model import Base, UserState
from domain.interfaces import IPostRepository

__author__ = 'anaeanet'


class User(Base):

    # TODO add post repository as 4th parameter

    def __init__(self, user_id, user_name, user_state, message_id=None, post_id=None):
        if not (isinstance(user_id, int)
                and isinstance(user_name, str)
                and isinstance(user_state, UserState)
                and (message_id is None or isinstance(message_id, int))
                and (post_id is None or isinstance(post_id, int))
                ):
            raise TypeError(
                "Invalid parameter type(s). Expected int, str, UserState, IPostRepository, int/None, int/None "
                + "but got %s, %s, %s, %s, %s."
                % (type(user_id).__name__, type(user_name).__name__, type(user_state).__name__,
                   type(message_id).__name__, type(post_id).__name__))
        elif len(user_name) == 0:
            raise ValueError("Invalid value provided: len(author_name) must be greater than 0.")

        self.__user_id = user_id
        self.__user_name = user_name
        self.__user_state = user_state
        self.__post_repository = None
        self.__message_id = message_id
        self.__post_id = post_id

    @property
    def user_id(self):
        return self.__user_id

    @property
    def user_name(self):
        return self.__user_name

    @property
    def user_state(self):
        return self.__user_state

    @property
    def post_repository(self):
        return self.__post_repository

    @property
    def message_id(self):
        return self.__message_id

    @property
    def post_id(self):
        return self.__post_id
