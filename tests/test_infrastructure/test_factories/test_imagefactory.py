import unittest

from domain.model import Image
from infrastructure.factories import ImageFactory

__author__ = 'anaeanet'


class ImageFactoryTest(unittest.TestCase):

    def setUp(self):
        self.image_gallery_id = 10
        self.image_id = 1
        self.image_name = "file_name"
        self.image_file = "file"
        self.image_thumb_id = "123_thumb_id"
        self.image_caption = "image_caption"

        self.args = [
            self.image_gallery_id
            , self.image_id
            , self.image_name
            , self.image_file
            , self.image_thumb_id
            , self.image_caption
        ]

        self.kwargs = {
            "image_id": self.image_id
            , "gallery_id": self.image_gallery_id
            , "name": self.image_name
            , "file": self.image_file
            , "thumb_id": self.image_thumb_id
            , "caption": self.image_caption
        }

        self.factory = ImageFactory()

    def test_factory_fails_for_invalid_arguments(self):
        with self.assertRaises(ValueError):
            self.factory.assemble(*self.args, **self.kwargs)

    def test_factory_makes_image_from_args(self):
        image = self.factory.assemble(*self.args)

        self.assertTrue(isinstance(image, Image))
        self.assertEqual(image.image_id, self.image_id)
        self.assertEqual(image.name, self.image_name)
        self.assertEqual(image.file, self.image_file)
        self.assertEqual(image.thumb_id, self.image_thumb_id)
        self.assertEqual(image.caption, self.image_caption)

    def test_factory_makes_image_from_kwargs(self):
        image = self.factory.assemble(**self.kwargs)

        self.assertTrue(isinstance(image, Image))
        self.assertEqual(image.image_id, self.image_id)
        self.assertEqual(image.name, self.image_name)
        self.assertEqual(image.file, self.image_file)
        self.assertEqual(image.thumb_id, self.image_thumb_id)
        self.assertEqual(image.caption, self.image_caption)

    def test_factory_disassembles_image_successfully(self):
        self.assertEqual(self.kwargs, self.factory.disassemble(self.factory.assemble(*self.args)))
        self.assertEqual(self.kwargs, self.factory.disassemble(self.factory.assemble(**self.kwargs)))


if __name__ == '__main__':
    unittest.main()
