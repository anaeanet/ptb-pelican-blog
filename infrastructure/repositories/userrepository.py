from domain.interfaces import IUserRepository

__author__ = 'anaeanet'


class UserRepository(IUserRepository):

    def __init__(self, persistence, factory):
        self.__persistence = persistence
        self.__factory = factory

    def get_users(self, **filters):
        users = []

        for user_data in self.__persistence.retrieve(**filters):
            users.append(self.__factory.assemble(**user_data))

        return users

    def get_user_by_id(self, user_id):
        return self.__factory.assemble(**self.__persistence.retrieve_by_id(user_id))

    def save_user(self, user):
        return self.__persistence.persist(**self.__factory.disassemble(user))

    def remove_user(self, user_id):
        return self.__persistence.delete(user_id)
