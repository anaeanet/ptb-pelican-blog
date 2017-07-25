import unittest

from infrastructure.factories import ImageFactory
from infrastructure.repositories import ImageRepository
from infrastructure.persistence import InMemoryImagePersistence

__author__ = 'anaeanet'


class ImageRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.image_gallery_id = 10
        self.image_id = 1
        self.image_name = "file_name"
        self.image_file = "file"
        self.image_thumb_id = "123_thumb_id"
        self.image_caption = "image_caption"

        self.factory = ImageFactory()
        self.repo = ImageRepository(InMemoryImagePersistence(), self.factory)

        self.image = self.factory.assemble(*[
            self.image_gallery_id
            , self.image_id
            , self.image_name
            , self.image_file
            , self.image_thumb_id
            , self.image_caption
        ])

    def test_image_added_successfully(self):
        self.assertTrue(self.repo.save_image(self.image))
        self.assertEqual(self.image, self.repo.get_images()[0])

    def test_added_image_can_be_retrieved_from_repo_by_id(self):
        self.assertTrue(self.repo.save_image(self.image))
        self.assertEqual(self.image, self.repo.get_image_by_id(self.image_id))

    def test_added_image_can_be_retrieved_from_repo_by_filter(self):
        self.assertTrue(self.repo.save_image(self.image))
        self.assertEqual(self.image, self.repo.get_images(image_id=self.image_id)[0])

    def test_image_can_be_deleted_from_repo(self):
        self.assertTrue(self.repo.save_image(self.image))
        self.assertTrue(self.repo.remove_image(self.image_id))

    def test_image_updated_successfully(self):
        self.assertTrue(self.repo.save_image(self.image))
        self.assertEqual(self.image, self.repo.get_image_by_id(self.image_id))

        updated_image = self.factory.assemble(*[
            self.image_gallery_id
            , self.image_id
            , self.image_name+"_updated"
            , self.image_file
            , self.image_thumb_id
            , self.image_caption+"_updated"
        ])

        self.assertTrue(self.repo.save_image(updated_image))
        self.assertEqual(updated_image, self.repo.get_image_by_id(self.image_id))
        self.assertNotEqual(self.image, self.repo.get_image_by_id(self.image_id))


if __name__ == '__main__':
    unittest.main()
