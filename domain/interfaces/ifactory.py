import abc

__author__ = 'anaeanet'


class IFactory(metaclass=abc.ABCMeta):

    @staticmethod
    def check_params(*args, **kwargs):
        if not (args or kwargs) or (args and kwargs):
            raise ValueError("Invalid parameter combination: Exactly one of *args or **kwargs must be specified.")

    @abc.abstractmethod
    def make(self, *args, **kwargs):
        self.check_params(*args, **kwargs)

        raise NotImplementedError

    @abc.abstractmethod
    def take_apart(self, item):
        raise NotImplementedError
