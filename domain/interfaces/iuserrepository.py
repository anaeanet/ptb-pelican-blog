import abc

__author__ = 'anaeanet'


class IUserRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_users(self, **filters):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user_by_id(self, user_id):
        raise NotImplementedError

    @abc.abstractmethod
    def save_user(self, user):
        raise NotImplementedError

    @abc.abstractmethod
    def update_user(self, user_id, **update_params):
        raise NotImplementedError

    @abc.abstractmethod
    def remove_user(self, user_id):
        raise NotImplementedError
