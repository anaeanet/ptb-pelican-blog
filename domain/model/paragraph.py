from domain.model import Base

__author__ = 'anaeanet'


class Paragraph(Base):

    def __init__(self, id, post_id, text):
        if not (isinstance(id, int)
                and isinstance(post_id, int)
                and isinstance(text, str)):
            raise TypeError(
                "Invalid parameter type(s). Expected int, int, str "
                + "but got %s, %s, %s."
                % (type(id).__name__, type(post_id).__name__, type(text).__name__))
        elif len(text) == 0:
            raise ValueError("Invalid value provided: len(text) must be greater than 0.")

        self.__paragraph_id = id
        self.__post_id = post_id
        self.__text = text

    @classmethod
    def properties(cls):
        return ["id", "post_id", "text"]

    @property
    def id(self):
        return self.__paragraph_id

    @property
    def post_id(self):
        return self.__post_id

    @property
    def text(self):
        return self.__text
