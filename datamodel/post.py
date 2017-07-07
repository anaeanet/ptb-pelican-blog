import datamodel
from datetime import datetime

__author__ = 'anaeanet'


class Post(datamodel.AbstractDatamodelObject):

    def __init__(self, create_timestamp, title, state, paragraphs=[], authors=[], tags=[], gallery=None, cover_image=None, publish_timestamp=None, predecessor_post=None):
        self.create_timestamp = create_timestamp
        self.title = title
        self.state = state
        self.paragraphs = paragraphs
        self.authors = authors
        self.tags = tags
        self.gallery = gallery
        self.cover_image = cover_image
        self.publish_timestamp = publish_timestamp
        self.predecessor_post = predecessor_post

    @staticmethod
    def de_json(data):
        """
        Args:
            data (dict):
        Returns:
            datamodel.Post:
        """
        if not data:
            return None

        data = super(Post, Post).de_json(data)
        data['create_timestamp'] = datetime.strptime(data.get('create_timestamp'), "%Y-%m-%d %H:%M:%S.%f")
        data['state'] = datamodel.PostState(data.get('state'))
        data['paragraphs'] = datamodel.Paragraph.de_list(data.get('paragraphs'))
        data['authors'] = datamodel.Author.de_list(data.get('authors'))
        data['tags'] = datamodel.Tag.de_list(data.get('tags'))
        data['gallery'] = datamodel.Gallery.de_json(data.get('gallery'))
        data['cover_image'] = datamodel.Image.de_json(data.get('cover_image'))
        data['publish_timestamp'] = None if data.get('publish_timestamp') is None else datetime.strptime(data.get('publish_timestamp'), "%Y-%m-%d %H:%M:%S.%f")
        data['predecessor_post'] = Post.de_json(data.get('predecessor_post'))

        return Post(**data)

    def to_dict(self):
        """
        Returns:
            dict:
        """
        data = super(Post, self).to_dict()

        data['create_timestamp'] = data.pop('create_timestamp', None)
        if data['create_timestamp'] is not None:
            data['create_timestamp'] = data['create_timestamp'].strftime("%Y-%m-%d %H:%M:%S.%f")
        data['title'] = data.pop('title', None)
        data['state'] = data.pop('state', None)
        if data['state'] is not None:
            data['state'] = data['state'].value
        data['paragraphs'] = [e.to_dict() for e in self.paragraphs]
        data['authors'] = [e.to_dict() for e in self.authors]
        data['tags'] = [e.to_dict() for e in self.tags]
        data['gallery'] = data.pop('gallery', None)
        data['cover_image'] = data.pop('cover_image', None)
        data['publish_timestamp'] = data.pop('publish_timestamp', None)
        if data['publish_timestamp'] is not None:
            data['publish_timestamp'] = data['publish_timestamp'].strftime("%Y-%m-%d %H:%M:%S.%f")
        data['predecessor_post'] = data.pop('predecessor_post', None)

        return data

    @staticmethod
    def de_list(data):
        """
        Args:
            data (list):
        Returns:
            List<datamodel.Post>:
        """
        if not data:
            return list()

        posts = list()
        for post in data:
            posts.append(Post.de_json(post))

        return posts
