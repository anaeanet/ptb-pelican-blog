import unittest
from infrastructure.persistence import InMemoryImagePersistence
from infrastructure.factories import ImageFactory

__author__ = 'anaeanet'


class InMemoryImagePersistenceTest(unittest.TestCase):

    def setUp(self):
        self.image_id = 1
        self.image_gallery_id = 10
        self.image_file_id = "123_file_id"
        self.image_name = "file_name"
        self.image_file = "file"
        self.image_thumb_id = "123_thumb_id"
        self.image_caption = "image_caption"

        self.image1 = ImageFactory().assemble(
            *[self.image_id, self.image_gallery_id, self.image_file_id, self.image_name, self.image_file, self.image_thumb_id, self.image_caption]
        )
        self.image2 = ImageFactory().assemble(
            *[2, self.image_gallery_id, self.image_file_id, self.image_name, self.image_file, self.image_thumb_id, self.image_caption]
        )

    def test_can_persist_and_retrieve_single_image(self):
        persistence = InMemoryImagePersistence()
        persistence.persist(self.image1.to_dict())

        self.assertEqual(self.image1.to_dict(), persistence.retrieve()[0])
        self.assertEqual(self.image1, ImageFactory().assemble(**persistence.retrieve()[0]))

    def test_can_persist_and_retrieve_multiple_images(self):
        persistence = InMemoryImagePersistence()
        persistence.persist(self.image1.to_dict())
        persistence.persist(self.image2.to_dict())

        self.assertEqual(self.image1.to_dict(), persistence.retrieve_by_id(self.image1.id))
        self.assertEqual(self.image2.to_dict(), persistence.retrieve_by_id(self.image2.id))
        self.assertEqual(self.image1, ImageFactory().assemble(**persistence.retrieve_by_id(self.image1.id)))
        self.assertEqual(self.image2, ImageFactory().assemble(**persistence.retrieve_by_id(self.image2.id)))

    def test_can_delete_image(self):
        persistence = InMemoryImagePersistence()
        persistence.persist(self.image1.to_dict())
        persistence.persist(self.image2.to_dict())

        self.assertTrue(persistence.delete(self.image1.id))
        self.assertTrue(persistence.delete(self.image2.id))

if __name__ == '__main__':
    unittest.main()
