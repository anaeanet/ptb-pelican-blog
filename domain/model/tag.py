from domain.model import Base

__author__ = 'anaeanet'


class Tag(Base):

    def __init__(self, post_id, tag_id, name):
        self.__post_id = post_id
        self.__tag_id = tag_id
        self.__name = name

    @property
    def post_id(self):
        return self.__post_id

    @property
    def tag_id(self):
        return self.__tag_id

    @property
    def name(self):
        return self.__name
