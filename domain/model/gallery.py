from domain.model import Base

__author__ = 'anaeanet'


class Gallery(Base):

    def __init__(self, post_id, title, image_repository, cover_image=None):
        self.__post_id = post_id
        self.__title = title
        self.__image_repository = image_repository
        self.__cover_image = cover_image

    @property
    def post_id(self):
        return self.__post_id

    @property
    def title(self):
        return self.__title

    @property
    def image_repository(self):
        return self.__image_repository

    @property
    def cover_image(self):
        return self.__cover_image
