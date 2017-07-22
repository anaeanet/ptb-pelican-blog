from domain.model import Base

__author__ = 'anaeanet'


class Tag(Base):

    def __init__(self, id, post_id, name):
        if not (isinstance(id, int)
                and isinstance(post_id, int)
                and isinstance(name, str)):
            raise TypeError(
                "Invalid parameter type(s). Expected int, int, str "
                + "but got %s, %s, %s."
                % (type(id).__name__, type(post_id).__name__, type(name).__name__))
        elif len(name) == 0:
            raise ValueError("Invalid value provided: len(name) must be greater than 0.")

        self.__id = id
        self.__post_id = post_id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def post_id(self):
        return self.__post_id

    @property
    def name(self):
        return self.__name
