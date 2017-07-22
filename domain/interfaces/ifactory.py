import abc

__author__ = 'anaeanet'


class IFactory(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def assemble(self, *args, **kwargs):
        self.check_params(*args, **kwargs)

        raise NotImplementedError

    @abc.abstractmethod
    def disassemble(self, item):
        raise NotImplementedError
