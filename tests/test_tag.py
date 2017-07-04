from tests.base import BaseTest
import datamodel
import unittest

__author__ = 'anaeanet'


class TagTest(BaseTest, unittest.TestCase):

    def setUp(self):
        self.name = "tag1"

        self.json_dict = {
            "name": self.name
        }

    def test_tag_de_json(self):
        tag = datamodel.Tag.de_json(self.json_dict)

        self.assertEqual(tag.name, self.name)

    def test_tag_to_json(self):
        tag = datamodel.Tag.de_json(self.json_dict)

        self.assertTrue(self.is_json(tag.to_json()))

    def test_tag_to_dict(self):
        tag = datamodel.Tag.de_json(self.json_dict)

        self.assertTrue(self.is_dict(tag.to_dict()))
        self.assertEqual(tag['name'], self.name)

    def test_equality(self):
        a = datamodel.Tag(self.name)
        b = datamodel.Tag(self.name)
        c = datamodel.Tag(None)
        e = datamodel.Author(self.name)

        self.assertEqual(a, b)
        self.assertEqual(hash(a), hash(b))
        self.assertIsNot(a, b)

        self.assertNotEqual(a, c)
        self.assertNotEqual(hash(a), hash(c))

        self.assertNotEqual(a, e)
        self.assertNotEqual(hash(a), hash(e))


if __name__ == '__main__':
    unittest.main()
