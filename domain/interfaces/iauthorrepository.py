import abc

__author__ = 'anaeanet'


class IAuthorRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_authors(self, **filters):
        raise NotImplementedError

    @abc.abstractmethod
    def get_author_by_id(self, author_id):
        raise NotImplementedError

    @abc.abstractmethod
    def add_author(self, author):
        raise NotImplementedError

    @abc.abstractmethod
    def remove_author(self, author_id):
        raise NotImplementedError
