import abc

__author__ = 'anaeanet'


class IParagraphRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_paragraphs(self, **filters):
        raise NotImplementedError

    @abc.abstractmethod
    def get_paragraph_by_id(self, paragraph_id):
        raise NotImplementedError

    @abc.abstractmethod
    def save_paragraph(self, paragraph):
        raise NotImplementedError

    @abc.abstractmethod
    def remove_paragraph(self, paragraph_id):
        raise NotImplementedError
