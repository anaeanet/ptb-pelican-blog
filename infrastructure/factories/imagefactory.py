from domain.interfaces import IFactory
from domain.model import Image

__author__ = 'anaeanet'


class ImageFactory(IFactory):

    def assemble(self, *args, **kwargs):

        if args and not kwargs:
            image = Image(*args)
        elif kwargs and not args:
            image = Image(**kwargs)
        else:
            raise ValueError("Invalid parameter combination. Exactly one of *args or **kwargs must be specified.")

        return image

    def disassemble(self, image):
        return image.to_dict()
