import abc
import json

__author__ = 'anaeanet'


class AbstractDatamodelObject(metaclass=abc.ABCMeta):

    def __str__(self):
        return str(self.to_dict())

    def __getitem__(self, item):
        x = self.__dict__
        return self.__dict__[item]

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return super().__eq__(other)

    def __ne__(self, other):
        if type(other) is type(self):
            return not self == other
        return super().__ne__(other)

    def __hash__(self):
        mod_dict = dict()
        for key, value in self.__dict__.items():
            if type(value) is not list:
                mod_dict[key] = value
        mod_dict[self.__class__.__name__] = self.__class__
        return hash(tuple(sorted(mod_dict.items())))

    @staticmethod
    def de_json(data):
        """
        Args:
            data (dict):
        Returns:
            dict:
        """
        if not data:
            return None

        data = data.copy()

        return data

    def to_json(self):
        """
        Returns:
            str:
        """
        return json.dumps(self.to_dict())

    def to_dict(self):
        """
        Returns:
            dict:
        """
        data = dict()

        for key in iter(self.__dict__):
            value = self.__dict__[key]
            if value is not None:
                if hasattr(value, 'to_dict'):
                    data[key] = value.to_dict()
                else:
                    data[key] = value

        return data
