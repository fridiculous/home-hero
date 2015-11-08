import json


class Property(object):

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.photos = kwargs.get('photos')

    def analyze(self):
        with open('hero/data/phoenix.json') as data_file:
            data = json.load(data_file)

        return data
