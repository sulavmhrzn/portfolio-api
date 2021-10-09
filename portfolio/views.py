from django.views import generic


from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import AboutMeSerializer, ContactMeSerializer
from .models import AboutMe, ContactMe
from .mixins import AdminOnlyBrowsableAPIMixin


class UnderDevelopment(generic.RedirectView):
    """Redirects to `/api/` url. Currently not implemented"""

    url = "/api/"


class About(AdminOnlyBrowsableAPIMixin, APIView):
    """Accepts only `GET` request."""

    def get(self, request):
        instance = AboutMe.objects.first()
        serialized = AboutMeSerializer(instance=instance)
        return Response(serialized.data)


class ContactMeView(APIView):
    """
    Accepts both GET and POST request.
    """

    def get(self, request):
        contact = ContactMe.objects.all()
        serializer = ContactMeSerializer(instance=contact, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContactMeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Success"})
        return Response(serializer.errors)
