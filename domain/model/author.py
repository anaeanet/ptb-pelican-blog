from domain.model import Base

__author__ = 'anaeanet'


class Author(Base):

    def __init__(self, post_id, author_id, name):
        self.__post_id = post_id
        self.__author_id = author_id
        self.__name = name

    @property
    def post_id(self):
        return self.__post_id

    @property
    def author_id(self):
        return self.__author_id

    @property
    def name(self):
        return self.__name
