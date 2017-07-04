from tests.base import BaseTest
import datamodel
import unittest

__author__ = 'anaeanet'


class GalleryTest(BaseTest, unittest.TestCase):

    def setUp(self):
        self.title = "gallery_title"
        self.images = [
            {
                "file_id": 1,
                "name": "image1.jpg",
                "file": "file1",
                "thumb_id": None,
                "caption": None
            },
            {
                "file_id": 2,
                "name": "image2.jpg",
                "file": "file3",
                "thumb_id": 5,
                "caption": None
            },
            {
                "file_id": 3,
                "name": "image3.jpg",
                "file": "file3",
                "thumb_id": 6,
                "caption": "caption3"
            },
            {
                "file_id": 4,
                "name": "image4.jpg",
                "file": "file4",
                "thumb_id": None,
                "caption": "caption4"
            }
        ]

        self.json_dict = {
            "title": self.title,
            "images": self.images
        }

    def test_gallery_de_json(self):
        gallery = datamodel.Gallery.de_json(self.json_dict)

        self.assertEqual(gallery.title, self.title)
        self.assertEqual(gallery.images, [datamodel.Image(**e) for e in self.images])

    def test_gallery_to_json(self):
        gallery = datamodel.Gallery.de_json(self.json_dict)

        self.assertTrue(self.is_json(gallery.to_json()))

    def test_gallery_to_dict(self):
        gallery = datamodel.Gallery.de_json(self.json_dict)

        self.assertTrue(self.is_dict(gallery.to_dict()))
        self.assertEqual(gallery['title'], self.title)
        self.assertEqual(gallery['images'], [datamodel.Image(**e) for e in self.images])

    def test_equality(self):
        a = datamodel.Gallery(self.title, None)
        b = datamodel.Gallery(self.title, None)
        c = datamodel.Gallery("gallery_title_2", None)
        e = datamodel.Tag(self.title)

        self.assertEqual(a, b)
        self.assertEqual(hash(a), hash(b))
        self.assertIsNot(a, b)

        self.assertNotEqual(a, c)
        self.assertNotEqual(hash(a), hash(c))

        self.assertNotEqual(a, e)
        self.assertNotEqual(hash(a), hash(e))


if __name__ == '__main__':
    unittest.main()
