from domain.model import Base

__author__ = 'anaeanet'


class Post(Base):

    def __init__(self, user_id, post_id, tmsp_creation, title, post_state
                 , author_repository, tag_repository, paragraph_repository
                 , gallery=None, base_post=None, tmsp_publish=None):
        self.__user_id = user_id
        self.__post_id = post_id
        self.__tmsp_creation = tmsp_creation
        self.__title = title
        self.__post_state = post_state
        self.__author_repository = author_repository
        self.__tag_repository = tag_repository
        self.__paragraph_repository = paragraph_repository
        self.__gallery = gallery
        self.__base_post = base_post
        self.__tmsp_publish = tmsp_publish

    @property
    def user_id(self):
        return self.__user_id

    @property
    def post_id(self):
        return self.__post_id

    @property
    def tmsp_creation(self):
        return self.__tmsp_creation

    @property
    def title(self):
        return self.__title

    @property
    def post_state(self):
        return self.__post_state

    @property
    def author_repository(self):
        return self.__author_repository

    @property
    def tag_repository(self):
        return self.__tag_repository

    @property
    def paragraph_repository(self):
        return self.__paragraph_repository

    @property
    def gallery(self):
        return self.__gallery

    @property
    def base_post(self):
        return self.__base_post

    @property
    def tmsp_publish(self):
        return self.__tmsp_publish
