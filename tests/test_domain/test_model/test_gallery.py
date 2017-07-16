import unittest
from domain.model import Gallery
from infrastructure.repositories import ImageRepository
from infrastructure.factories import ImageFactory

__author__ = 'anaeanet'


class GalleryTest(unittest.TestCase):

    def setUp(self):
        self.gallery_id = 1
        self.gallery_post_id = 1
        self.gallery_title = "gallery_title"
        self.gallery_image_repository = ImageRepository()

        self.image_id = 1
        self.image_gallery_id = 10
        self.image_file_id = "123_file_id"
        self.image_name = "file_name"
        self.image_file = "file"
        self.image_thumb_id = "123_thumb_id"
        self.image_caption = "image_caption"

        self.image = ImageFactory().make(*[self.image_id, self.image_gallery_id, self.image_file_id, self.image_name, self.image_file, self.image_thumb_id, self.image_caption])

    def test_gallery_creation_fails_for_invalid_arguments(self):
        with self.assertRaises(TypeError):
            Gallery(None, self.gallery_post_id, self.gallery_title, self.gallery_image_repository)

        with self.assertRaises(TypeError):
            Gallery(self.gallery_id, None, self.gallery_title, self.gallery_image_repository)

        with self.assertRaises(TypeError):
            Gallery(self.gallery_id, self.gallery_post_id, None, self.gallery_image_repository)

        with self.assertRaises(TypeError):
            Gallery(self.gallery_id, self.gallery_post_id, self.gallery_title, None)

        with self.assertRaises(ValueError):
            Gallery(self.gallery_id, self.gallery_post_id, "", self.gallery_image_repository)

    def test_gallery_creation_successful(self):
        gallery = Gallery(self.gallery_id, self.gallery_post_id, self.gallery_title, self.gallery_image_repository)

        self.assertTrue(isinstance(gallery, Gallery))

    def test_gallery_equality_with_empty_repositories(self):
        gallery1 = Gallery(self.gallery_id, self.gallery_post_id, self.gallery_title, self.gallery_image_repository)
        gallery2 = Gallery(self.gallery_id, self.gallery_post_id, self.gallery_title, self.gallery_image_repository)

        self.assertEqual(gallery1, gallery2)

    def test_gallery_equality_with_non_empty_repositories(self):
        self.gallery_image_repository.add_image(self.image)

        gallery1 = Gallery(self.gallery_id, self.gallery_post_id, self.gallery_title, self.gallery_image_repository)
        gallery2 = Gallery(self.gallery_id, self.gallery_post_id, self.gallery_title, self.gallery_image_repository)

        self.assertEqual(gallery1, gallery2)


if __name__ == '__main__':
    unittest.main()
