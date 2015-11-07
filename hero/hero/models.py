class Property(object):

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.photos = kwargs.get('photos')

    def analyze(self):
        return {'result': 12344}
