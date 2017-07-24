import unittest
from domain.model import User, UserState
from infrastructure.factories import UserFactory
from infrastructure.repositories import PostRepository

__author__ = 'anaeanet'


class UserFactoryTest(unittest.TestCase):

    def setUp(self):
        self.user_id = 1
        self.user_name = "anaea"
        self.user_state = UserState.MAIN_MENU
        #self.post_repository = PostRepository(None, None)
        self.message_id = None
        self.post_id = None

        self.user = User(self.user_id
                         , self.user_name
                         , self.user_state
                         #, self.post_repository
                         , message_id=self.message_id
                         , post_id=self.post_id)

        self.args = [self.user_id
                         , self.user_name
                         , self.user_state.value
                         #, self.post_repository
                         , self.message_id
                         , self.post_id]

        self.kwargs = self.user.to_dict()

    def test_factory_fails_for_invalid_arguments(self):
        with self.assertRaises(ValueError):
            UserFactory().assemble()

        with self.assertRaises(ValueError):
            UserFactory().assemble(*self.args, **self.kwargs)

    def test_factory_makes_user_from_args(self):
        user = UserFactory().assemble(*self.args)

        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.user_id, self.user_id)
        self.assertEqual(user.user_name, self.user_name)
        self.assertEqual(user.user_state, self.user_state)
        #self.assertEqual(user.post_repository, self.post_repository)
        self.assertEqual(user.message_id, self.message_id)
        self.assertEqual(user.post_id, self.post_id)

    def test_factory_makes_user_from_kwargs(self):
        user = UserFactory().assemble(**self.kwargs)

        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.user_id, self.user_id)
        self.assertEqual(user.user_name, self.user_name)
        self.assertEqual(user.user_state, self.user_state)
        #self.assertEqual(user.post_repository, self.post_repository)
        self.assertEqual(user.message_id, self.message_id)
        self.assertEqual(user.post_id, self.post_id)


if __name__ == '__main__':
    unittest.main()
