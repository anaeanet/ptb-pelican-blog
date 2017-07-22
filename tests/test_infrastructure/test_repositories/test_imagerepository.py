import unittest

from infrastructure.factories import ImageFactory
from infrastructure.repositories import ImageRepository

__author__ = 'anaeanet'


class ImageRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.image_id = 1
        self.image_gallery_id = 10
        self.image_file_id = "123_file_id"
        self.image_name = "file_name"
        self.image_file = "file"
        self.image_thumb_id = "123_thumb_id"
        self.image_caption = "image_caption"

        self.image = ImageFactory().assemble(*[self.image_id, self.image_gallery_id, self.image_file_id, self.image_name, self.image_file, self.image_thumb_id, self.image_caption])

    def test_persisted_image_can_be_retrieved_from_persistence(self):
        repo = ImageRepository()
        repo.add_image(self.image)

        self.assertEqual(self.image, repo.get_images()[0])

    def test_persisted_image_can_be_retrieved_from_persistence_by_id(self):
        repo = ImageRepository()
        repo.add_image(self.image)

        self.assertEqual(self.image, repo.get_image_by_id(self.image_id))

    def test_persisted_image_can_be_retrieved_from_persistence_by_filter(self):
        repo = ImageRepository()
        repo.add_image(self.image)

        self.assertEqual(self.image, repo.get_images(**{"id": self.image.id})[0])

    def test_image_can_be_deleted_from_repo(self):
        repo = ImageRepository()
        repo.add_image(self.image)

        self.assertTrue(repo.remove_image(self.image.id))
        self.assertEqual(repo.get_images(), [])


if __name__ == '__main__':
    unittest.main()
