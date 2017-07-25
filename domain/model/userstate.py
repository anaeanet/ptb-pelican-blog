from enum import Enum

__author__ = 'anaeanet'


class UserState(Enum):
    INIT, MAIN_MENU = range(2)

    def to_dict(self):
        return self.value
