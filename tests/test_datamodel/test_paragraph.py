import unittest

import datamodel
from tests.test_datamodel.base import BaseTest

__author__ = 'anaeanet'


class ParagraphTest(BaseTest, unittest.TestCase):

    def setUp(self):
        self.text = "author1"

        self.json_dict = {
            "text": self.text
        }

    def test_paragraph_de_json(self):
        paragraph = datamodel.Paragraph.de_json(self.json_dict)

        self.assertEqual(paragraph.text, self.text)

    def test_paragraph_to_json(self):
        paragraph = datamodel.Paragraph.de_json(self.json_dict)

        self.assertTrue(self.is_json(paragraph.to_json()))

    def test_paragraph_to_dict(self):
        paragraph = datamodel.Paragraph.de_json(self.json_dict)

        self.assertTrue(self.is_dict(paragraph.to_dict()))
        self.assertEqual(paragraph['text'], self.text)

    def test_equality(self):
        a = datamodel.Paragraph(self.text)
        b = datamodel.Paragraph(self.text)
        c = datamodel.Paragraph(None)
        e = datamodel.Tag(self.text)

        self.assertEqual(a, b)
        self.assertEqual(hash(a), hash(b))
        self.assertIsNot(a, b)

        self.assertNotEqual(a, c)
        self.assertNotEqual(hash(a), hash(c))

        self.assertNotEqual(a, e)
        self.assertNotEqual(hash(a), hash(e))


if __name__ == '__main__':
    unittest.main()
