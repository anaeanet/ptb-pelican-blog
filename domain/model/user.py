from domain.model import Base
from domain.interfaces import IPostRepository

__author__ = 'anaeanet'


class User(Base):

    def __init__(self, id, author_name, post_repository):
        if not (isinstance(id, int)
                and isinstance(author_name, str)
                and isinstance(post_repository, IPostRepository)):
            raise TypeError(
                "Invalid parameter type(s). Expected int, str, IPostRepository "
                + "but got %s, %s, %s."
                % (type(id).__name__, type(author_name).__name__, type(post_repository).__name__))
        elif len(author_name) == 0:
            raise ValueError("Invalid value provided: len(author_name) must be greater than 0.")

        self.__user_id = id
        self.__author_name = author_name
        self.__post_repository = post_repository

    @classmethod
    def properties(cls):
        return ["id", "author_name"]

    @property
    def id(self):
        return self.__post_id

    @property
    def author_name(self):
        return self.__author_name

    @property
    def post_repository(self):
        return self.__post_repository

    def __eq__(self, other):
        if isinstance(self, User) and type(self) == type(other):
            return self.to_dict() == other.to_dict() \
                   and self.post_repository.get_posts() == other.post_repository.get_posts()
        else:
            return super().__eq__(other)