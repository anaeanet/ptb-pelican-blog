from .abstractdatamodelobject import AbstractDatamodelObject
from datetime import datetime

__author__ = 'anaeanet'


class Paragraph(AbstractDatamodelObject):

    def __init__(self, text):
        self.text = text

    @staticmethod
    def de_json(data):
        """
        Args:
            data (dict):
        Returns:
            datamodel.Paragraph:
        """
        if not data:
            return None

        return Paragraph(**data)

    @staticmethod
    def de_list(data):
        """
        Args:
            data (list):
        Returns:
            List<datamodel.Paragraph>:
        """
        if not data:
            return list()

        paragraphs = list()
        for paragraph in data:
            paragraphs.append(Paragraph.de_json(paragraph))

        return paragraphs