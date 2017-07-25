import unittest
from domain.model import User, UserState
from infrastructure.persistence import SQLUserPersistence
from infrastructure.factories import UserFactory

__author__ = 'anaeanet'


class SQLUserPersistenceTest(unittest.TestCase):

    def setUp(self):
        self.user_id = 1
        self.user_name = "anaea"
        self.user_state = 0
        self.message_id = None
        self.post_id = None

        self.user_data = {
            "user_id": self.user_id
            , "user_name": self.user_name
            , "user_state": self.user_state
            , "message_id": self.message_id
            , "post_id": self.post_id
        }

        self.user_data2 = {
            "user_id": 2
            , "user_name": self.user_name
            , "user_state": self.user_state
            , "message_id": self.message_id
            , "post_id": self.post_id
        }

        self.persistence = SQLUserPersistence(":memory:")

    def test_can_persist_and_retrieve_single_user(self):
        self.persistence.persist(**self.user_data)

        self.assertEqual(self.user_data, self.persistence.retrieve()[0])

    def test_can_persist_and_retrieve_multiple_users(self):
        self.persistence.persist(**self.user_data)
        self.persistence.persist(**self.user_data2)

        self.assertEqual(self.user_data, self.persistence.retrieve_by_id(self.user_data["user_id"]))
        self.assertEqual(self.user_data2, self.persistence.retrieve_by_id(self.user_data2["user_id"]))

    def test_can_delete_user(self):
        self.persistence.persist(**self.user_data)
        self.persistence.persist(**self.user_data2)

        self.assertTrue(self.persistence.delete(self.user_data["user_id"]))
        self.assertTrue(self.persistence.delete(self.user_data2["user_id"]))

if __name__ == '__main__':
    unittest.main()
