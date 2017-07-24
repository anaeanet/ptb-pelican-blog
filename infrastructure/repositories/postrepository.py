from domain.interfaces import IPostRepository

__author__ = 'anaeanet'


class PostRepository(IPostRepository):

    def __init__(self, persistence, factory):
        self.__persistence = persistence
        self.__factory = factory

    def get_posts(self, **filters):
        posts = []

        for post_data in self.__persistence.retrieve(**filters):
            posts.append(self.__factory.assemble(**post_data))

        return posts

    def get_post_by_id(self, id):
        return self.__factory.assemble(**self.__persistence.retrieve_by_id(id))

    def add_post(self, post):
        return self.__persistence.persist(self.__factory.disassemble(post))

    def remove_post(self, id):
        return self.__persistence.delete(id)
