from enum import Enum

__author__ = 'anaeanet'


class UserState(Enum):
    MAIN_MENU = 0

    def to_dict(self):
        return self.value
