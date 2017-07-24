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
        # self.post_repository = PostRepository(None, None)
        self.message_id = None
        self.post_id = None

        self.user = UserFactory().assemble(*[
            self.user_id, self.user_name, self.user_state, self.message_id, self.post_id
        ])

        self.persistence = SQLUserPersistence("test.db")
        self.repo = UserRepository(self.persistence, UserFactory())

    def test_persisted_user_can_be_retrieved_from_persistence(self):
        self.repo.add_user(self.user)

        self.assertEqual(self.user, self.repo.get_users()[0])

    def test_persisted_user_can_be_retrieved_from_persistence_by_id(self):
        self.repo.add_user(self.user)

        self.assertEqual(self.user, self.repo.get_user_by_id(self.user_id))

    def test_persisted_user_can_be_retrieved_from_persistence_by_filter(self):
        self.repo.add_user(self.user)

        self.assertEqual(self.user, self.repo.get_users(**{"user_id": self.user_id})[0])

    def test_user_can_be_deleted_from_repo(self):
        self.repo.add_user(self.user)

        self.assertTrue(self.repo.remove_user(self.user_id))


if __name__ == '__main__':
    unittest.main()
