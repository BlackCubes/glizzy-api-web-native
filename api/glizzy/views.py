from rest_framework import generics, permissions

from .models import Glizzy
from .serializers import GlizzySerializer

from core.mixins import MultipleFieldLookupMixin


class GlizzyDetailView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    """
    A generic view that finds a particular object given either a ``pk`` or
    ``slug`` from the URL, if it exists.

    NOTE: Only a GET request.
    """

    permission_classes = (permissions.AllowAny,)
    queryset = Glizzy.objects.all()
    serializer_class = GlizzySerializer
    lookup_fields = (
        "pk",
        "slug",
    )
