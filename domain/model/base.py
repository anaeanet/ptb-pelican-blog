import abc

__author__ = 'anaeanet'


class Base(metaclass=abc.ABCMeta):

    @classmethod
    def properties(cls):
        raise NotImplementedError

    def to_dict(self):
        return dict([(prop, getattr(self, prop)) for prop in self.properties()])

    def __eq__(self, other):
        if isinstance(self, Base) and type(self) == type(other):
            return self.to_dict() == other.to_dict()
        else:
            return super().__eq__(other)

    def __ne__(self, other):
        return not self == other
