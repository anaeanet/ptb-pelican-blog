from domain.model import Base

__author__ = 'anaeanet'


class User(Base):

    # TODO add post repository as 4th parameter

    def __init__(self, user_id, user_name, user_state, message_id=None, post_id=None):
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
