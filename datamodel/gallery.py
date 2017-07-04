from .abstractdatamodelobject import AbstractDatamodelObject
from .image import Image

__author__ = 'anaeanet'


class Gallery(AbstractDatamodelObject):

    def __init__(self, title, images=None):
        self.title = title
        self.images = images or list()

    @staticmethod
    def de_json(data):
        """
        Args:
            data (dict):
        Returns:
            datamodel.Gallery:
        """
        if not data:
            return None

        data = super(Gallery, Gallery).de_json(data)
        data['images'] = Image.de_list(data.get('images'))

        return Gallery(**data)

    def to_dict(self):
        """
        Returns:
            dict:
        """
        data = super(Gallery, self).to_dict()

        data['title'] = data.pop('title', None)
        data['images'] = [e.to_dict() for e in self.images]

        return data
