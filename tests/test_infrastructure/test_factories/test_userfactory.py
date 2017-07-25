import unittest
from domain.model import User
from infrastructure.factories import UserFactory

__author__ = 'anaeanet'


class UserFactoryTest(unittest.TestCase):

    def setUp(self):
        self.user_id = 1
        self.user_name = "anaea"
        self.user_state = 0
        self.message_id = None
        self.post_id = None

        self.args = [
            self.user_id
            , self.user_name
            , self.user_state
            , self.message_id
            , self.post_id
        ]

        self.kwargs = {
            "user_id": self.user_id
            , "user_name": self.user_name
            , "user_state": self.user_state
            , "message_id": self.message_id
            , "post_id": self.post_id
        }

        self.factory = UserFactory()

    def test_factory_fails_for_invalid_arguments(self):
        with self.assertRaises(ValueError):
            self.factory.assemble()

        with self.assertRaises(ValueError):
            self.factory.assemble(*self.args, **self.kwargs)

    def test_factory_makes_user_from_args(self):
        user = self.factory.assemble(*self.args)

        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.user_id, self.user_id)
        self.assertEqual(user.user_name, self.user_name)
        self.assertEqual(user.user_state.value, self.user_state)
        self.assertEqual(user.message_id, self.message_id)
        self.assertEqual(user.post_id, self.post_id)

    def test_factory_makes_user_from_kwargs(self):
        user = self.factory.assemble(**self.kwargs)

        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.user_id, self.user_id)
        self.assertEqual(user.user_name, self.user_name)
        self.assertEqual(user.user_state.value, self.user_state)
        self.assertEqual(user.message_id, self.message_id)
        self.assertEqual(user.post_id, self.post_id)

    def test_factory_disassembles_user_successfully(self):
        self.assertEqual(self.kwargs, self.factory.disassemble(self.factory.assemble(*self.args)))
        self.assertEqual(self.kwargs, self.factory.disassemble(self.factory.assemble(**self.kwargs)))


if __name__ == '__main__':
    unittest.main()
