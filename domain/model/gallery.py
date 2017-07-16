from domain.model import Base
from domain.interfaces import IImageRepository

__author__ = 'anaeanet'


class Gallery(Base):

    def __init__(self, id, post_id, title, image_repository):
        if not (isinstance(id, int) and isinstance(post_id, int) and isinstance(title, str) and isinstance(image_repository, IImageRepository)):
            raise TypeError("Invalid parameter type(s). Expected int, int, str, IImageRepository but got %s, %s, %s, %s."
                            % (type(id).__name__, type(post_id).__name__, type(title).__name__, type(image_repository).__name__))
        elif len(title) == 0:
            raise ValueError("Invalid value provided: len(title) must be greater than 0.")

        self.__gallery_id = id
        self.__post_id = post_id
        self.__title = title
        self.__image_repository = image_repository

    @classmethod
    def properties(cls):
        return ["id", "post_id", "title"]

    @property
    def id(self):
        return self.__gallery_id

    @property
    def post_id(self):
        return self.__post_id

    @property
    def title(self):
        return self.__title

    @property
    def image_repository(self):
        return self.__image_repository

    def __eq__(self, other):
        if isinstance(self, Gallery) and type(self) == type(other):
            return self.to_dict() == other.to_dict() \
                   and self.image_repository.get_images() == other.image_repository.get_images()
        else:
            return super().__eq__(other)
