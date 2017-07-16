import abc

__author__ = 'anaeanet'


class IPostRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_posts(self, **filters):
        raise NotImplementedError

    @abc.abstractmethod
    def get_post_by_id(self, id):
        raise NotImplementedError

    @abc.abstractmethod
    def add_post(self, post):
        raise NotImplementedError

    @abc.abstractmethod
    def remove_post(self, id):
        raise NotImplementedError
