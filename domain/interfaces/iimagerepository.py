import abc

__author__ = 'anaeanet'


class IImageRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_images(self, **filters):
        raise NotImplementedError

    @abc.abstractmethod
    def get_image_by_id(self, id):
        raise NotImplementedError

    @abc.abstractmethod
    def add_image(self, image):
        raise NotImplementedError

    @abc.abstractmethod
    def remove_image(self, id):
        raise NotImplementedError
