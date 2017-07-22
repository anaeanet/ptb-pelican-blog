import abc

__author__ = 'anaeanet'


class Base(metaclass=abc.ABCMeta):

    def to_dict(self):
        data = dict()

        for key in iter(self.__dict__):
            value = self.__dict__[key]
            if value is not None:

                # strip any class name prefix from the attribute name
                param_name = key if key.find("__") < 0 else key[key.find("__")+2:]

                if hasattr(value, 'to_dict'):
                    data[param_name] = value.to_dict()
                else:
                    data[param_name] = value

        return data

    def __eq__(self, other):
        if isinstance(self, Base) and type(self) == type(other):
            return self.to_dict() == other.to_dict()
        else:
            return super().__eq__(other)

    def __ne__(self, other):
        return not self == other
