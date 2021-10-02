from django.views import generic


from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import AboutMeSerializer
from .models import AboutMe
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
