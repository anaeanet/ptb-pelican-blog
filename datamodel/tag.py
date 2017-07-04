from .abstractdatamodelobject import AbstractDatamodelObject

__author__ = 'anaeanet'


class Tag(AbstractDatamodelObject):

    def __init__(self, name):
        self.name = name

    @staticmethod
    def de_json(data):
        """
        Args:
            data (dict):
        Returns:
            datamodel.Tag:
        """
        if not data:
            return None

        return Tag(**data)

    @staticmethod
    def de_list(data):
        """
        Args:
            data (list):
        Returns:
            List<datamodel.Tag>:
        """
        if not data:
            return list()

        tags = list()
        for tag in data:
            tags.append(Tag.de_json(tag))

        return tags
