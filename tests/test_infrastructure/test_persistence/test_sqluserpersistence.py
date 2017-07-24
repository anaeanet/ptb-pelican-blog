import unittest
from domain.model import User, UserState
from infrastructure.persistence import SQLUserPersistence
from infrastructure.factories import UserFactory
from infrastructure.repositories import PostRepository

__author__ = 'anaeanet'


class SQLUserPersistenceTest(unittest.TestCase):

    def setUp(self):
        self.user_id = 1
        self.user_name = "anaea"
        self.user_state = UserState.MAIN_MENU
        #self.post_repository = PostRepository(None, None)
        self.message_id = None
        self.post_id = None

        self.user1 = User(self.user_id
                          , self.user_name
                          , self.user_state
                          #, self.post_repository
                          , message_id=self.message_id
                          , post_id=self.post_id)

        self.user2 = User(2
                          , self.user_name
                          , self.user_state
                          # , self.post_repository
                          , message_id=self.message_id
                          , post_id=self.post_id)

        self.persistence = SQLUserPersistence("test.db")

    def test_can_persist_and_retrieve_single_image(self):
        self.persistence.persist(UserFactory().disassemble(self.user1))

        self.assertEqual(self.user1, UserFactory().assemble(*self.persistence.retrieve()[0]))

    def test_can_persist_and_retrieve_multiple_images(self):
        self.persistence.persist(UserFactory().disassemble(self.user1))
        self.persistence.persist(UserFactory().disassemble(self.user2))

        self.assertEqual(self.user1, UserFactory().assemble(*self.persistence.retrieve_by_id(self.user1.user_id)))
        self.assertEqual(self.user2, UserFactory().assemble(*self.persistence.retrieve_by_id(self.user2.user_id)))

    def test_can_delete_image(self):
        self.persistence.persist(UserFactory().disassemble(self.user1))
        self.persistence.persist(UserFactory().disassemble(self.user2))

        self.assertTrue(self.persistence.delete(self.user1.user_id))
        self.assertTrue(self.persistence.delete(self.user2.user_id))

if __name__ == '__main__':
    unittest.main()
