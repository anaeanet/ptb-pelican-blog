import unittest
from domain.model import Image

__author__ = 'anaeanet'


class ImageTest(unittest.TestCase):

    def setUp(self):
        self.image_gallery_id = 10
        self.image_id = 1
        self.image_name = "file_name"
        self.image_file = "file"
        self.image_thumb_id = "123_thumb_id"
        self.image_caption = "image_caption"

    def test_image_creation_successful(self):
        image = Image(self.image_gallery_id
                      , self.image_id
                      , self.image_name
                      , self.image_file
                      , thumb_id=self.image_thumb_id
                      , caption=self.image_caption)

        self.assertTrue(isinstance(image, Image))
        self.assertEqual(image.image_id, self.image_id)
        self.assertEqual(image.gallery_id, self.image_gallery_id)
        self.assertEqual(image.name, self.image_name)
        self.assertEqual(image.file, self.image_file)
        self.assertEqual(image.thumb_id, self.image_thumb_id)
        self.assertEqual(image.caption, self.image_caption)

    def test_image_equality(self):
        image = Image(self.image_gallery_id
                      , self.image_id
                      , self.image_name
                      , self.image_file
                      , thumb_id=self.image_thumb_id
                      , caption=self.image_caption)
        image2 = Image(self.image_gallery_id
                      , self.image_id
                      , self.image_name
                      , self.image_file
                      , thumb_id=self.image_thumb_id
                      , caption=self.image_caption)

        self.assertEqual(image, image2)


if __name__ == '__main__':
    unittest.main()
