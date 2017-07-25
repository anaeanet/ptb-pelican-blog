from enum import Enum

__author__ = 'anaeanet'


class PostState(Enum):
    DRAFT = "draft"
    PUBLISHED = "published"

    def to_dict(self):
        return self.value