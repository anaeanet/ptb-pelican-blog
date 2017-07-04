from tests.base import BaseTest
import datamodel
import unittest

__author__ = 'anaeanet'


class ImageTest(BaseTest, unittest.TestCase):

    def setUp(self):
        self.file_id = 1
        self.name = "image.jpg"
        self.file = "abcdefgh"
        self.thumb_id = "2"
        self.caption = "somecaption"

        self.json_dict = {
            "file_id": self.file_id,
            "name": self.name,
            "file": self.file,
            "thumb_id": self.thumb_id,
            "caption": self.caption
        }

    def test_image_de_json(self):
        image = datamodel.Image.de_json(self.json_dict)

        self.assertEqual(image.file_id, self.file_id)
        self.assertEqual(image.name, self.name)
        self.assertEqual(image.file, self.file)
        self.assertEqual(image.thumb_id, self.thumb_id)
        self.assertEqual(image.caption, self.caption)

    def test_image_de_json_without_thumb_id(self):
        json_dict = self.json_dict
        del (json_dict["thumb_id"])

        image = datamodel.Image.de_json(json_dict)

        self.assertEqual(image.file_id, self.file_id)
        self.assertEqual(image.name, self.name)
        self.assertEqual(image.file, self.file)
        self.assertIsNone(image.thumb_id)
        self.assertEqual(image.caption, self.caption)

    def test_image_de_json_without_caption(self):
        json_dict = self.json_dict
        del (json_dict["caption"])

        image = datamodel.Image.de_json(json_dict)

        self.assertEqual(image.file_id, self.file_id)
        self.assertEqual(image.name, self.name)
        self.assertEqual(image.file, self.file)
        self.assertEqual(image.thumb_id, self.thumb_id)
        self.assertIsNone(image.caption)

    def test_image_to_json(self):
        image = datamodel.Image.de_json(self.json_dict)

        self.assertTrue(self.is_json(image.to_json()))

    def test_image_to_dict(self):
        image = datamodel.Image.de_json(self.json_dict)

        self.assertTrue(self.is_dict(image.to_dict()))
        self.assertEqual(image['file_id'], self.file_id)
        self.assertEqual(image['name'], self.name)
        self.assertEqual(image['file'], self.file)
        self.assertEqual(image['thumb_id'], self.thumb_id)
        self.assertEqual(image['caption'], self.caption)

    def test_equality(self):
        a = datamodel.Image(self.file_id, self.name, self.file, thumb_id=self.thumb_id, caption=self.caption)
        b = datamodel.Image(self.file_id, self.name, self.file, thumb_id=self.thumb_id, caption=self.caption)
        c = datamodel.Image(self.file_id, self.name, self.file)
        e = datamodel.Tag(self.name)

        self.assertEqual(a, b)
        self.assertEqual(hash(a), hash(b))
        self.assertIsNot(a, b)

        self.assertNotEqual(a, c)
        self.assertNotEqual(hash(a), hash(c))

        self.assertNotEqual(a, e)
        self.assertNotEqual(hash(a), hash(e))


if __name__ == '__main__':
    unittest.main()
