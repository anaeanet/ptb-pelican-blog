import abc

__author__ = 'anaeanet'


class IUserRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_user(self, **filters):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user_by_id(self, id):
        raise NotImplementedError

    @abc.abstractmethod
    def add_user(self, conversation):
        raise NotImplementedError

    @abc.abstractmethod
    def remove_user(self, id):
        raise NotImplementedError
