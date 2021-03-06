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

        for image_data in self.__persistence.retrieve(**filters):
            images.append(self.__factory.assemble(**image_data))

        return images

    def get_image_by_id(self, image_id):
        return self.__factory.assemble(**self.__persistence.retrieve_by_id(image_id))

    def save_image(self, image):
        return self.__persistence.persist(**image.to_dict())

    def update_image(self, image_id, **update_params):
        return self.__persistence.persist(image_id=image_id, **update_params)

    def remove_image(self, image_id):
        return self.__persistence.delete(image_id)
