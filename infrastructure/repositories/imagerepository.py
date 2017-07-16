from domain.interfaces import IImageRepository
from infrastructure.factories import ImageFactory
from infrastructure.persistence import InMemoryImagePersistence

__author__ = 'anaeanet'


class ImageRepository(IImageRepository):

    def __init__(self, persistence=None, factory=None):
        self.__persistence = InMemoryImagePersistence() if persistence is None else persistence
        self.__factory = ImageFactory() if factory is None else factory

    def get_images(self, **filters):
        images = []

        for raw_img in self.__persistence.retrieve(**filters):
            images.append(self.__factory.make(**raw_img))

        return images

    def get_image_by_id(self, id):
        return self.__factory.make(**self.__persistence.retrieve_by_id(id))

    def add_image(self, image):
        return self.__persistence.persist(self.__factory.take_apart(image))

    def remove_image(self, id):
        return self.__persistence.delete(id)
