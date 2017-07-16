import unittest
from domain.model import Image

__author__ = 'anaeanet'


class ImageTest(unittest.TestCase):

    def setUp(self):
        self.image_id = 1
        self.image_gallery_id = 10
        self.image_file_id = "123_file_id"
        self.image_name = "file_name"
        self.image_file = "file"
        self.image_thumb_id = "123_thumb_id"
        self.image_caption = "image_caption"

    def test_gallery_creation_fails_for_invalid_arguments(self):
        with self.assertRaises(TypeError):
            Image(None
                  , self.image_gallery_id
                  , self.image_file_id
                  , self.image_name
                  , self.image_file
                  , thumb_id=self.image_thumb_id
                  , caption=self.image_caption)

        with self.assertRaises(TypeError):
            Image(self.image_id
                  , None
                  , self.image_file_id
                  , self.image_name
                  , self.image_file
                  , thumb_id=self.image_thumb_id
                  , caption=self.image_caption)

        with self.assertRaises(TypeError):
            Image(self.image_id
                  , self.image_gallery_id
                  , None
                  , self.image_name
                  , self.image_file
                  , thumb_id=self.image_thumb_id
                  , caption=self.image_caption)

        with self.assertRaises(TypeError):
            Image(self.image_id
                  , self.image_gallery_id
                  , self.image_file_id
                  , None
                  , self.image_file
                  , thumb_id=self.image_thumb_id
                  , caption=self.image_caption)

        with self.assertRaises(TypeError):
            Image(self.image_id
                  , self.image_gallery_id
                  , self.image_file_id
                  , self.image_name
                  , None
                  , thumb_id=self.image_thumb_id
                  , caption=self.image_caption)

        with self.assertRaises(TypeError):
            Image(self.image_id
                  , self.image_gallery_id
                  , self.image_file_id
                  , self.image_name
                  , self.image_file
                  , thumb_id=1
                  , caption=self.image_caption)

        with self.assertRaises(TypeError):
            Image(self.image_id
                  , self.image_gallery_id
                  , self.image_file_id
                  , self.image_name
                  , self.image_file
                  , thumb_id=self.image_thumb_id
                  , caption=2)

        with self.assertRaises(ValueError):
            Image(self.image_id
                  , self.image_gallery_id
                  , ""
                  , self.image_name
                  , self.image_file
                  , thumb_id=self.image_thumb_id
                  , caption=self.image_caption)

        with self.assertRaises(ValueError):
            Image(self.image_id
                  , self.image_gallery_id
                  , self.image_file_id
                  , ""
                  , self.image_file
                  , thumb_id=self.image_thumb_id
                  , caption=self.image_caption)

        with self.assertRaises(ValueError):
            Image(self.image_id
                  , self.image_gallery_id
                  , self.image_file_id
                  , self.image_name
                  , self.image_file
                  , thumb_id=""
                  , caption=self.image_caption)

        with self.assertRaises(ValueError):
            Image(self.image_id
                  , self.image_gallery_id
                  , self.image_file_id
                  , self.image_name
                  , self.image_file
                  , thumb_id=self.image_thumb_id
                  , caption="")

    def test_image_creation_successful(self):
        image = Image(self.image_id
                      , self.image_gallery_id
                      , self.image_file_id
                      , self.image_name
                      , self.image_file
                      , thumb_id=self.image_thumb_id
                      , caption=self.image_caption)

        self.assertTrue(isinstance(image, Image))
        self.assertEqual(image.id, self.image_id)
        self.assertEqual(image.gallery_id, self.image_gallery_id)
        self.assertEqual(image.file_id, self.image_file_id)
        self.assertEqual(image.name, self.image_name)
        self.assertEqual(image.file, self.image_file)
        self.assertEqual(image.thumb_id, self.image_thumb_id)
        self.assertEqual(image.caption, self.image_caption)

    def test_image_equality(self):
        image = Image(self.image_id
                      , self.image_gallery_id
                      , self.image_file_id
                      , self.image_name
                      , self.image_file
                      , thumb_id=self.image_thumb_id
                      , caption=self.image_caption)
        image2 = Image(self.image_id
                      , self.image_gallery_id
                      , self.image_file_id
                      , self.image_name
                      , self.image_file
                      , thumb_id=self.image_thumb_id
                      , caption=self.image_caption)

        self.assertEqual(image, image2)


if __name__ == '__main__':
    unittest.main()
