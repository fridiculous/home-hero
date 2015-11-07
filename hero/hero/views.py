from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from hero.models import Property


class PropertyViewSet(APIView):
    """
    API endpoint that allows properties to be viewed or edited.
    """
    def get(self, request, *args, **kw):
        # Process any get params if any
        propertyid = request.GET.get('id', None)
        photos = request.GET.get('photos', None)

        # Any URL parameters get passed in **kw
        myproperty = Property(id=propertyid, photos=photos)
        result = myproperty.analyze()
        response = Response(result, status=status.HTTP_200_OK)
        return response
