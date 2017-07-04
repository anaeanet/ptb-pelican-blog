from bot import BotState
from datamodel import Post

__author__ = "anaeanet"


class BotUser:

    def __init__(self, state, message=None, selected_post=None, posts=None):
        self.__state = state
        self.__message = message
        self.__selected_post = selected_post
        self.__posts = [] if posts is None else [p for p in posts]

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, new_state):
        self.__state = new_state if isinstance(new_state, BotState) else self.state

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, new_message):
        self.__message = new_message if isinstance(new_message, int) else self.message

    @property
    def selected_post(self):
        return self.__selected_post

    @selected_post.setter
    def selected_post(self, new_selected_post):
        self.__selected_post = new_selected_post if isinstance(new_selected_post, Post) else self.selected_post

    @property
    def posts(self):
        return self.__posts

    def add_post(self, post):
        return self.__posts.append(post)

    def remove_post(self, post):
        return self.__posts.remove(post)
