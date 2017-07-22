from domain.model import Base, UserState
from domain.interfaces import IPostRepository

__author__ = 'anaeanet'


class User(Base):

    def __init__(self, id, author_name, post_repository, user_state=None, message_id=None, post_id=None):
        if not (isinstance(id, int)
                and isinstance(author_name, str)
                and isinstance(post_repository, IPostRepository)
                and (user_state is None or isinstance(user_state, UserState))
                and (message_id is None or isinstance(message_id, int))
                and (post_id is None or isinstance(post_id, int))
                ):
            raise TypeError(
                "Invalid parameter type(s). Expected int, str, IPostRepository, UserState/None, int/None, int/None "
                + "but got %s, %s, %s, %s, %s, %s."
                % (type(id).__name__, type(author_name).__name__, type(post_repository).__name__,
                   type(user_state).__name__, type(message_id).__name__, type(post_id).__name__))
        elif len(author_name) == 0:
            raise ValueError("Invalid value provided: len(author_name) must be greater than 0.")

        self.__user_id = id
        self.__author_name = author_name
        self.__post_repository = post_repository
        self.__user_state = user_state
        self.__message_id = message_id
        self.__post_id = post_id

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

    @property
    def user_state(self):
        return self.__user_state

    @property
    def message_id(self):
        return self.__message_id

    @property
    def post_id(self):
        return self.__post_id

    def __eq__(self, other):
        if isinstance(self, User) and type(self) == type(other):
            return self.to_dict() == other.to_dict() \
                   and self.post_repository.get_posts() == other.post_repository.get_posts()
        else:
            return super().__eq__(other)
