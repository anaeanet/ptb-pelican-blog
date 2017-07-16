import abc

__author__ = 'anaeanet'


class IImagePersistence(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def persist(self, image_dict):
        raise NotImplementedError

    @abc.abstractmethod
    def retrieve(self, **filters):
        raise NotImplementedError

    @abc.abstractmethod
    def retrieve_by_id(self, id):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, id):
        raise NotImplementedError
