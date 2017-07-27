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

    def persist(self, **image_data):
        pk = "image_id"

        image = self.__data[image_data[pk]] if pk in image_data and image_data[pk] in self.__data else None
        if not image:
            self.__data[image_data[pk]] = image_data
        else:
            for key, value in image_data.items():
                self.__data[image_data[pk]][key] = value

        return True

    def retrieve(self, **filters):
        return [v for v in self.__data.values() if self.__matches_filters(v, **filters)]

    def retrieve_by_id(self, image_id):
        return self.__data[image_id] if image_id in self.__data else {}

    def delete(self, image_id):
        result = False

        if image_id in self.__data:
            self.__data.pop(image_id)
            result = True

        return result
