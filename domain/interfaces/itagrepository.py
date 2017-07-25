import abc

__author__ = 'anaeanet'


class ITagRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_tags(self, **filters):
        raise NotImplementedError

    @abc.abstractmethod
    def get_tag_by_id(self, tag_id):
        raise NotImplementedError

    @abc.abstractmethod
    def add_tag(self, tag):
        raise NotImplementedError

    @abc.abstractmethod
    def remove_tag(self, tag_id):
        raise NotImplementedError
