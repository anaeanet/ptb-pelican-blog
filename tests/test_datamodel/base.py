import json

__author__ = 'anaeanet'


class BaseTest:

    @staticmethod
    def is_json(string):
        try:
            json.loads(string)
        except ValueError:
            return False

        return True

    @staticmethod
    def is_dict(dictionary):
        if isinstance(dictionary, dict):
            return True

        return False
