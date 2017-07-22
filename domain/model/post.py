from domain.model import Base, PostState, Gallery
from domain.interfaces import IAuthorRepository, ITagRepository, IParagraphRepository
from datetime import datetime

__author__ = 'anaeanet'


class Post(Base):

    def __init__(self, id, user_id, tmsp_creation, title, post_state
                 , author_repository, tag_repository, paragraph_repository
                 , gallery=None, base_post=None, tmsp_publish=None):
        if not (isinstance(id, int)
                and isinstance(user_id, int)
                and isinstance(tmsp_creation, datetime)
                and isinstance(title, str)
                and isinstance(post_state, PostState)
                and isinstance(author_repository, IAuthorRepository)
                and isinstance(tag_repository, ITagRepository)
                and isinstance(paragraph_repository, IParagraphRepository)
                and (gallery is None or isinstance(gallery, Gallery))
                and (base_post is None or isinstance(base_post, Post))
                and (tmsp_publish is None or isinstance(tmsp_publish, datetime))):
            raise TypeError(
                "Invalid parameter type(s). Expected int, int, datetime, str, PostState, IAuthorRepository, "
                + "ITagRepository, IParagraphRepository, Gallery/None, Post/None, datetime/None "
                + "but got %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s."
                % (type(id).__name__, type(user_id).__name__, type(tmsp_creation).__name__, type(title).__name__
                   , type(post_state).__name__, type(author_repository).__name__, type(tag_repository).__name__
                   , type(paragraph_repository).__name__, type(gallery).__name__
                   , type(base_post).__name__, type(tmsp_publish).__name__))
        elif len(title) == 0:
            raise ValueError("Invalid value provided: len(title) must be greater than 0.")

        self.__id = id
        self.__user_id = user_id
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
    def id(self):
        return self.__id

    @property
    def user_id(self):
        return self.__user_id

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
