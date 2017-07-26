from domain.model import Base

__author__ = 'anaeanet'


class User(Base):

    def __init__(self, user_id, user_name, user_state=None, message_id=None, post_id=None):
        self.__user_id = user_id
        self.__user_name = user_name
        self.__user_state = user_state
        self.__posts = None
        self.__message_id = message_id
        self.__post_id = post_id

    @property
    def user_id(self):
        return self.__user_id

    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, value):
        self.__user_name = value

    @property
    def user_state(self):
        return self.__user_state

    @user_state.setter
    def user_state(self, value):
        self.__user_state = value

    @property
    def posts(self):
        return self.__posts

    @property
    def message_id(self):
        return self.__message_id

    @message_id.setter
    def message_id(self, value):
        self.__message_id = value

    @property
    def post_id(self):
        return self.__post_id

    @post_id.setter
    def post_id(self, value):
        self.__post_id = value
