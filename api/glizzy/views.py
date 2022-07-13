from rest_framework import generics, permissions

from .models import Glizzy
from .serializers import GlizzySerializer

from core.mixins import MultipleFieldLookupMixin


class RetrieveGlizzyView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    """
    A generic view that retrieves all objects from the Glizzy model, or finds
    a particular object given either a ``pk``  or ``slug`` from the URL.

    NOTE: Only a GET request.
    """

    permission_classes = (permissions.AllowAny,)
    queryset = Glizzy.objects.all()
    serializer_class = GlizzySerializer
    lookup_fields = (
        "pk",
        "slug",
    )
