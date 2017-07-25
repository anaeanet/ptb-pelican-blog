import unittest
from infrastructure.persistence import InMemoryImagePersistence
from infrastructure.factories import ImageFactory

__author__ = 'anaeanet'


class InMemoryImagePersistenceTest(unittest.TestCase):

    def setUp(self):
        self.image_id = 1
        self.image_gallery_id = 10
        self.image_name = "file_name"
        self.image_file = "file"
        self.image_thumb_id = "123_thumb_id"
        self.image_caption = "image_caption"

        self.image_data = {
            "image_id": self.image_id
            , "gallery_id": self.image_gallery_id
            , "name": self.image_name
            , "file": self.image_file
            , "thumb_id": self.image_thumb_id
            , "caption": self.image_caption
        }

        self.image_data2 = {
            "image_id": 2
            , "gallery_id": self.image_gallery_id
            , "name": self.image_name
            , "file": self.image_file
            , "thumb_id": self.image_thumb_id
            , "caption": self.image_caption
        }

        self.persistence = InMemoryImagePersistence()

    def test_can_persist_and_retrieve_single_image(self):
        self.persistence.persist(**self.image_data)

        self.assertEqual(self.image_data, self.persistence.retrieve()[0])

    def test_can_persist_and_retrieve_multiple_images(self):
        self.persistence.persist(**self.image_data)
        self.persistence.persist(**self.image_data2)

        self.assertEqual(self.image_data, self.persistence.retrieve_by_id(self.image_data["image_id"]))
        self.assertEqual(self.image_data2, self.persistence.retrieve_by_id(self.image_data2["image_id"]))

    def test_can_delete_image(self):
        self.persistence.persist(**self.image_data)
        self.persistence.persist(**self.image_data2)

        self.assertTrue(self.persistence.delete(self.image_data["image_id"]))
        self.assertTrue(self.persistence.delete(self.image_data2["image_id"]))

if __name__ == '__main__':
    unittest.main()
