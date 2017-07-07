from .abstractdatamodelobject import AbstractDatamodelObject

__author__ = 'anaeanet'


class Author(AbstractDatamodelObject):

    def __init__(self, name):
        self.name = name

    @staticmethod
    def de_json(data):
        """
        Args:
            data (dict):
        Returns:
            datamodel.Author:
        """
        if not data:
            return None

        return Author(**data)

    @staticmethod
    def de_list(data):
        """
        Args:
            data (list):
        Returns:
            List<datamodel.Author>:
        """
        if not data:
            return list()

        authors = list()
        for author in data:
            authors.append(Author.de_json(author))

        return authors
