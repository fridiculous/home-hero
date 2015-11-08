from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from hero.models import Property, User


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


class UserViewSet(APIView):
    """
    API endpoint that allows user's interactions
    To Send email to user, hit api/email with the user's email and user's name
    """
    def get(self, request, *args, **kw):
        # Process any get params if any
        name = request.GET.get('name', None)
        email = request.GET.get('email', None)
        properties = Property().analyze()[:5]
        user = User(
            name=name,
            email=email,
            city='Phoenix',
            phone='213-301-1234',
            profile_photo='',
            address='1202 W Encanto Blvd, Phoenix AZ 85007',
            latitude='33.474533',
            longitude='-112.0899603',
            property_type='Single Family Home',
            properties=properties
        )
        result = user.send_email()
        response = Response(result, status=status.HTTP_200_OK)
        return response
