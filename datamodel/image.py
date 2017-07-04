from .abstractdatamodelobject import AbstractDatamodelObject

__author__ = 'anaeanet'


class Image(AbstractDatamodelObject):

    def __init__(self, file_id, name, file, thumb_id=None, caption=None):
        self.file_id = file_id
        self.name = name
        self.file = file
        self.thumb_id = thumb_id
        self.caption = caption

    @staticmethod
    def de_json(data):
        """
        Args:
            data (dict):
        Returns:
            datamodel.Image:
        """
        if not data:
            return None

        return Image(**data)

    @staticmethod
    def de_list(data):
        """
        Args:
            data (list):
        Returns:
            List<datamodel.Image>:
        """
        if not data:
            return list()

        images = list()
        for image in data:
            images.append(Image.de_json(image))

        return images
