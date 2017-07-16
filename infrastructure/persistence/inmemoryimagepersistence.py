from infrastructure.interfaces import IImagePersistence

__author__ = 'anaeanet'


class InMemoryImagePersistence(IImagePersistence):

    def __init__(self):
        self.__data = {}

    @staticmethod
    def __matches_filters(image_data, **filters):
        result = True

        for key, value in filters.items():
            if not (key in image_data and image_data[key] == value):
                result = False
                break

        return result

    def persist(self, image_dict):
        result = False

        if image_dict and "id" in image_dict:
            self.__data[image_dict["id"]] = image_dict
            result = True

        return result

    def retrieve(self, **filters):
        return [v for v in self.__data.values() if InMemoryImagePersistence.__matches_filters(v, **filters)]

    def retrieve_by_id(self, id):
        return self.__data[id]

    def delete(self, id):
        result = False

        if id in self.__data:
            self.__data.pop(id)
            result = True

        return result
