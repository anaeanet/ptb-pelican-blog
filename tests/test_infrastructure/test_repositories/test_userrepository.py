import unittest

from infrastructure.factories import UserFactory
from infrastructure.repositories import UserRepository
from infrastructure.persistence import SQLUserPersistence

__author__ = 'anaeanet'


class UserRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.user_id = 1
        self.user_name = "anaea"
        self.user_state = 0
        self.message_id = None
        self.post_id = None

        self.factory = UserFactory()
        self.repo = UserRepository(SQLUserPersistence(":memory:"), self.factory)

        self.user = self.factory.assemble(*[
            self.user_id, self.user_name, self.user_state, self.message_id, self.post_id
        ])

    def test_user_added_successfully(self):
        self.assertTrue(self.repo.save_user(self.user))
        self.assertEqual(self.user, self.repo.get_users()[0])

    def test_added_user_can_be_retrieved_from_repo_by_id(self):
        self.assertTrue(self.repo.save_user(self.user))
        self.assertEqual(self.user, self.repo.get_user_by_id(self.user_id))

    def test_added_user_can_be_retrieved_from_repo_by_filter(self):
        self.assertTrue(self.repo.save_user(self.user))
        self.assertEqual(self.user, self.repo.get_users(user_id=self.user_id)[0])

    def test_user_can_be_deleted_from_repo(self):
        self.assertTrue(self.repo.save_user(self.user))
        self.assertTrue(self.repo.remove_user(self.user_id))

    def test_user_updated_successfully(self):
        self.assertTrue(self.repo.save_user(self.user))
        self.assertEqual(self.user, self.repo.get_user_by_id(self.user_id))

        updated_user = self.factory.assemble(*[
            self.user_id, self.user_name+"_updated", self.user_state, 10, 100
        ])

        self.assertTrue(self.repo.save_user(updated_user))
        self.assertEqual(updated_user, self.repo.get_user_by_id(self.user_id))
        self.assertNotEqual(self.user, self.repo.get_user_by_id(self.user_id))

if __name__ == '__main__':
    unittest.main()
