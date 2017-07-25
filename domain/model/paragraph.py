from domain.model import Base

__author__ = 'anaeanet'


class Paragraph(Base):

    def __init__(self, post_id, paragraph_id, text):
        self.__post_id = post_id
        self.__paragraph_id = paragraph_id
        self.__text = text

    @property
    def post_id(self):
        return self.__post_id

    @property
    def paragraph_id(self):
        return self.__paragraph_id

    @property
    def text(self):
        return self.__text
