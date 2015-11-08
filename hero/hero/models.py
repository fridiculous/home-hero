import json


class Property(object):

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.photos = kwargs.get('photos')

    def analyze(self):
        with open('/data/phoenix.json') as data_file:
            data = json.load(data_file)

        return data


class User(object):

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.phone = kwargs.get('phone')
        self.profile_photo = kwargs.get('profile_photo')
        self.address = kwargs.get('address')
        self.latitude = kwargs.get('latitude')
        self.longitude = kwargs.get('longitude')
        self.property_type = kwargs.get('property_type')
