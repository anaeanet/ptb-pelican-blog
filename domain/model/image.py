from domain.model import Base

__author__ = 'anaeanet'


class Image(Base):

    def __init__(self, gallery_id, image_id, name, file, thumb_id=None, caption=None):
        self.__gallery_id = gallery_id
        self.__image_id = image_id
        self.__name = name
        self.__file = file
        self.__thumb_id = thumb_id
        self.__caption = caption

    @property
    def gallery_id(self):
        return self.__gallery_id

    @property
    def image_id(self):
        return self.__image_id

    @property
    def name(self):
        return self.__name

    @property
    def file(self):
        return self.__file

    @property
    def thumb_id(self):
        return self.__thumb_id

    @property
    def caption(self):
        return self.__caption
