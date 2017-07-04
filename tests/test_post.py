from tests.base import BaseTest
from datetime import datetime
import datamodel
import unittest

__author__ = 'anaeanet'


class PostTest(BaseTest, unittest.TestCase):

    def setUp(self):
        self.create_timestamp = datetime.now()
        self.title = "post_title"
        self.state = datamodel.PostState.DRAFT
        self.paragraphs = [
            {
                "text": "paragraph1"
            },
            {
                "text": "paragraph2"
            }
        ]
        self.authors = [
            {
                "name": "author1"
            },
            {
                "name": "author2"
            }
        ]
        self.tags = [
            {
                "name": "tage1"
            },
            {
                "name": "tag2"
            }
        ]
        self.gallery = None
        self.cover_image = None
        self.publish_timestamp = None
        self.predecessor_post = None

        self.json_dict = {
            "create_timestamp": self.create_timestamp.strftime("%Y-%m-%d %H:%M:%S.%f"),
            "title": self.title,
            "state": self.state.value,
            "paragraphs": self.paragraphs,
            "authors": self.authors,
            "tags": self.tags,
            "gallery": self.gallery,
            "cover_image": self.cover_image,
            "publish_timestamp": self.publish_timestamp,
            "predecessor_post": self.predecessor_post
        }

    def test_post_de_json(self):
        post = datamodel.Post.de_json(self.json_dict)

        self.assertEqual(post.create_timestamp, self.create_timestamp)
        self.assertEqual(post.title, self.title)
        self.assertEqual(post.state, self.state)
        self.assertEqual(post.paragraphs, [datamodel.Paragraph(**e) for e in self.paragraphs])
        self.assertEqual(post.authors, [datamodel.Author(**e) for e in self.authors])
        self.assertEqual(post.tags, [datamodel.Tag(**e) for e in self.tags])
        self.assertEqual(post.gallery, self.gallery)
        self.assertEqual(post.cover_image, self.cover_image)
        self.assertEqual(post.publish_timestamp, self.publish_timestamp)
        self.assertEqual(post.predecessor_post, self.predecessor_post)

    def test_post_to_json(self):
        post = datamodel.Post.de_json(self.json_dict)

        self.assertTrue(self.is_json(post.to_json()))

    def test_post_to_dict(self):
        post = datamodel.Post.de_json(self.json_dict)

        self.assertTrue(self.is_dict(post.to_dict()))
        self.assertEqual(post['create_timestamp'], self.create_timestamp)
        self.assertEqual(post['title'], self.title)
        self.assertEqual(post['state'], self.state)
        self.assertEqual(post['paragraphs'], [datamodel.Paragraph(**e) for e in self.paragraphs])
        self.assertEqual(post['authors'], [datamodel.Author(**e) for e in self.authors])
        self.assertEqual(post['tags'], [datamodel.Tag(**e) for e in self.tags])
        self.assertEqual(post['gallery'], self.gallery)
        self.assertEqual(post['cover_image'], self.cover_image)
        self.assertEqual(post['publish_timestamp'], self.publish_timestamp)
        self.assertEqual(post['predecessor_post'], self.predecessor_post)

    def test_equality(self):
        a = datamodel.Post(self.create_timestamp, self.title, self.state)
        b = datamodel.Post(self.create_timestamp, self.title, self.state)
        c = datamodel.Post(self.create_timestamp, "post_title_2", self.state)
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
