import unittest
from domain.model import User, UserState
from infrastructure.repositories import PostRepository

__author__ = 'anaeanet'


class UserTest(unittest.TestCase):

    def setUp(self):
        self.user_id = 1
        self.user_name = "anaea"
        self.user_state = UserState.MAIN_MENU
        #self.post_repository = PostRepository(None, None)
        self.message_id = None
        self.post_id = None

    def test_user_creation_fails_for_invalid_arguments(self):
        with self.assertRaises(TypeError):
            User(None
                 , self.user_name
                 , self.user_state
                 #, self.post_repository
                 , message_id=self.message_id
                 , post_id=self.post_id)

        with self.assertRaises(TypeError):
            User(self.user_id
                 , None
                 , self.user_state
                 #, self.post_repository
                 , message_id=self.message_id
                 , post_id=self.post_id)

        with self.assertRaises(ValueError):
            User(self.user_id
                 , ""
                 , self.user_state
                 #, self.post_repository
                 , message_id=self.message_id
                 , post_id=self.post_id)

        with self.assertRaises(TypeError):
            User(self.user_id
                 , self.user_name
                 , None
                 #, self.post_repository
                 , message_id=self.message_id
                 , post_id=self.post_id)

        with self.assertRaises(TypeError):
            User(self.user_id
                 , self.user_name
                 , 100
                 #, self.post_repository
                 , message_id=self.message_id
                 , post_id=self.post_id)

        with self.assertRaises(TypeError):
            User(self.user_id
                 , self.user_name
                 , self.user_state
                 #, self.post_repository
                 , message_id="123"
                 , post_id=self.post_id)

        with self.assertRaises(TypeError):
            User(self.user_id
                 , self.user_name
                 , self.user_state
                 #, self.post_repository
                 , message_id=self.message_id
                 , post_id="123")

    def test_user_creation_successful(self):
        user = User(self.user_id
                    , self.user_name
                    , self.user_state
                    #, self.post_repository
                    , message_id=self.message_id
                    , post_id=self.post_id)

        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.user_id, self.user_id)
        self.assertEqual(user.user_name, self.user_name)
        self.assertEqual(user.user_state, self.user_state)
        #self.assertEqual(user.post_repository, self.post_repository)
        self.assertEqual(user.message_id, self.message_id)
        self.assertEqual(user.post_id, self.post_id)

    def test_user_equality(self):
        user1 = User(self.user_id
                     , self.user_name
                     , self.user_state
                     #, self.post_repository
                     , message_id=self.message_id
                     , post_id=self.post_id)
        user2 = User(self.user_id
                     , self.user_name
                     , self.user_state
                     #, self.post_repository
                     , message_id=self.message_id
                     , post_id=self.post_id)

        self.assertEqual(user1, user2)


if __name__ == '__main__':
    unittest.main()
