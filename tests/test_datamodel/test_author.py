import unittest

import datamodel
from tests.test_datamodel.base import BaseTest

__author__ = 'anaeanet'


class AuthorTest(BaseTest, unittest.TestCase):

    def setUp(self):
        self.name = "author1"

        self.json_dict = {
            "name": self.name
        }

    def test_author_de_json(self):
        author = datamodel.Author.de_json(self.json_dict)

        self.assertEqual(author.name, self.name)

    def test_author_to_json(self):
        author = datamodel.Author.de_json(self.json_dict)

        self.assertTrue(self.is_json(author.to_json()))

    def test_author_to_dict(self):
        author = datamodel.Author.de_json(self.json_dict)

        self.assertTrue(self.is_dict(author.to_dict()))
        self.assertEqual(author['name'], self.name)

    def test_equality(self):
        a = datamodel.Author(self.name)
        b = datamodel.Author(self.name)
        c = datamodel.Author(None)
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
