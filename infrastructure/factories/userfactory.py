from domain.model import User, UserState
from domain.interfaces import IFactory

__author__ = 'anaeanet'


class UserFactory(IFactory):

    def assemble(self, *args, **kwargs):

        if not (args or kwargs):
            user = None

        elif args and not kwargs:
            user = User(args[0], args[1], UserState(args[2]), args[3], args[4])

        elif kwargs and not args:

            for key, value in kwargs.items():
                kwargs[key] = UserState(value) if key == "user_state" and value is not None else value

            user = User(**kwargs)

        else:
            raise ValueError("Invalid parameter combination. Exactly one of *args or **kwargs must be specified.")

        return user

    def disassemble(self, user):
        return {key: value for key, value in user.to_dict().items() if key != "posts"}
