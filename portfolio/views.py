from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import AboutMeSerializer
from .models import AboutMe
from .mixins import AdminOnlyBrowsableAPIMixin


class About(AdminOnlyBrowsableAPIMixin, APIView):
    """Accepts only `GET` request."""

    def get(self, request):
        instance = AboutMe.objects.first()
        serialized = AboutMeSerializer(instance=instance)
        return Response(serialized.data)
