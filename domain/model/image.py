from domain.model import Base

__author__ = 'anaeanet'


class Image(Base):

    def __init__(self, id, gallery_id, file_id, name, file, thumb_id=None, caption=None):
        if not (isinstance(id, int)
                and isinstance(gallery_id, int)
                and isinstance(file_id, str)
                and isinstance(name, str)
                and file is not None
                and (thumb_id is None or isinstance(thumb_id, str))
                and (caption is None or isinstance(caption, str))):
            raise TypeError(
                "Invalid parameter type(s). Expected int, int, str, str, not None, str/None, str/None "
                + "but got %s, %s, %s, %s, %s, %s, %s."
                % (type(id).__name__, type(gallery_id).__name__, type(file_id).__name__, type(name).__name__
                               , type(file).__name__
                               , type(thumb_id).__name__
                               , type(caption).__name__))
        elif len(file_id) == 0:
            raise ValueError("Invalid value provided: len(file_id) must be greater than 0.")
        elif len(name) == 0:
            raise ValueError("Invalid value provided: len(name) must be greater than 0.")
        elif thumb_id is not None and len(thumb_id) == 0:
            raise ValueError("Invalid value provided: len(thumb_id) must be greater than 0.")
        elif caption is not None and len(caption) == 0:
            raise ValueError("Invalid value provided: len(caption) must be greater than 0.")

        self.__image_id = id
        self.__gallery_id = gallery_id
        self.__file_id = file_id
        self.__name = name
        self.__file = file
        self.__thumb_id = thumb_id
        self.__caption = caption

    @classmethod
    def properties(cls):
        return ["id", "gallery_id", "file_id", "name", "file", "thumb_id", "caption"]

    @property
    def id(self):
        return self.__image_id

    @property
    def gallery_id(self):
        return self.__gallery_id

    @property
    def file_id(self):
        return self.__file_id

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
