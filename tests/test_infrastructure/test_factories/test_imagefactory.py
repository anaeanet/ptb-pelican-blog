import unittest

from domain.model import Image
from infrastructure.factories import ImageFactory

__author__ = 'anaeanet'


class ImageFactoryTest(unittest.TestCase):

    def setUp(self):
        self.image_id = 1
        self.image_gallery_id = 10
        self.image_file_id = "123_file_id"
        self.image_name = "file_name"
        self.image_file = "file"
        self.image_thumb_id = "123_thumb_id"
        self.image_caption = "image_caption"

        self.image = Image(self.image_id,
                           self.image_gallery_id,
                           self.image_file_id,
                           self.image_name,
                           self.image_file,
                           thumb_id=self.image_thumb_id,
                           caption=self.image_caption)

        self.args = [self.image_id, self.image_gallery_id, self.image_file_id, self.image_name, self.image_file, self.image_thumb_id, self.image_caption]
        self.kwargs = self.image.to_dict()

    def test_factory_fails_for_invalid_arguments(self):
        with self.assertRaises(ValueError):
            ImageFactory().assemble()

        with self.assertRaises(TypeError):
            ImageFactory().assemble(*self.args[:4])

        with self.assertRaises(TypeError):
            ImageFactory().assemble(**{k:v for k, v in self.kwargs.items() if k != "id"})

        with self.assertRaises(ValueError):
            ImageFactory().assemble(*self.args, **self.kwargs)

    def test_factory_makes_image_from_args(self):
        image = ImageFactory().assemble(*self.args)

        self.assertTrue(isinstance(image, Image))
        self.assertEqual(image.id, self.image_id)
        self.assertEqual(image.file_id, self.image_file_id)
        self.assertEqual(image.name, self.image_name)
        self.assertEqual(image.file, self.image_file)
        self.assertEqual(image.thumb_id, self.image_thumb_id)
        self.assertEqual(image.caption, self.image_caption)

    def test_factory_makes_image_from_kwargs(self):
        image = ImageFactory().assemble(**self.kwargs)

        self.assertTrue(isinstance(image, Image))
        self.assertEqual(image.id, self.image_id)
        self.assertEqual(image.file_id, self.image_file_id)
        self.assertEqual(image.name, self.image_name)
        self.assertEqual(image.file, self.image_file)
        self.assertEqual(image.thumb_id, self.image_thumb_id)
        self.assertEqual(image.caption, self.image_caption)


if __name__ == '__main__':
    unittest.main()
