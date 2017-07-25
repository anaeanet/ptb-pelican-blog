from infrastructure.interfaces import IUserPersistence
from infrastructure.persistence import DBHelper

__author__ = 'anaeanet'


class SQLUserPersistence(IUserPersistence):

    def __init__(self, db_name):
        self.__db = DBHelper(db_name)

    def persist(self, **user_data):
        pk = "user_id"

        user = self.__db.get_user(user_data[pk] if pk in user_data else -1)
        if user is None:
            return self.__db.add_user(**user_data)
        else:
            return self.__db.update_user(**user_data)

    def retrieve(self, **filters):
        return [v for v in self.__db.get_users(**filters)]

    def retrieve_by_id(self, user_id):
        return self.__db.get_user(user_id)

    def delete(self, user_id):
        return self.__db.delete_user(user_id)
