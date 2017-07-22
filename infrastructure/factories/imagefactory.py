from domain.interfaces import IFactory
from domain.model import Image

__author__ = 'anaeanet'


class ImageFactory(IFactory):

    def assemble(self, *args, **kwargs):
        keys = Image.properties()
        values = []

        if args and not kwargs:
            for i in range(min(len(args), len(keys))):
                values.append(args[i])
        elif kwargs and not args:
            for k in keys:
                if k in kwargs:
                    values.append(kwargs[k])
        else:
            raise ValueError("Invalid parameter combination. Exactly one of *args or **kwargs must be specified.")

        if len(values) == len(keys):
            item = Image(values[0], values[1], values[2], values[3], values[4], values[5], values[6])
        else:
            raise ValueError("Incorrect number of values provided: Expected %i but got %i. %s = %s."
                             % (len(keys), len(values), "args" if args else "kwargs", args if args else kwargs))

        return item

    def disassemble(self, image):
        return image.to_dict()
