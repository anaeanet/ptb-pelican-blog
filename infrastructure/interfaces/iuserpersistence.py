import abc

__author__ = 'anaeanet'


class IUserPersistence(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def persist(self, user_data):
        raise NotImplementedError

    @abc.abstractmethod
    def retrieve(self, **filters):
        raise NotImplementedError

    @abc.abstractmethod
    def retrieve_by_id(self, user_id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, user_id):
        raise NotImplementedError
