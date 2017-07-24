from domain.interfaces import IImageRepository
from infrastructure.factories import ImageFactory
from infrastructure.persistence import InMemoryImagePersistence

__author__ = 'anaeanet'


class ImageRepository(IImageRepository):

    def __init__(self, persistence, factory):
        self.__persistence = persistence
        self.__factory = factory

    def get_images(self, **filters):
        images = []

        for raw_img in self.__persistence.retrieve(**filters):
            images.append(self.__factory.assemble(**raw_img))

        return images

    def get_image_by_id(self, id):
        return self.__factory.assemble(**self.__persistence.retrieve_by_id(id))

    def add_image(self, image):
        return self.__persistence.persist(self.__factory.disassemble(image))

    def remove_image(self, id):
        return self.__persistence.delete(id)
