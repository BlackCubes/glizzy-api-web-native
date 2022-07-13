from rest_framework import generics, permissions

from .models import Glizzy
from .serializers import GlizzySerializer

from core.mixins import MultipleFieldLookupMixin


class GlizzyListView(generics.ListAPIView):
    """
    A generic view that finds all objects from the Glizzy model.

    NOTE: Only a GET request.
    """

    permission_classes = (permissions.AllowAny,)
    queryset = Glizzy.objects.all()
    serializer_class = GlizzySerializer


class GlizzyDetailView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    """
    A generic view that finds a particular object from the Glizzy model given
    either a ``pk`` or ``slug`` from the URL, if it exists.

    NOTE: Only a GET request.
    """

    permission_classes = (permissions.AllowAny,)
    queryset = Glizzy.objects.all()
    serializer_class = GlizzySerializer
    lookup_fields = (
        "pk",
        "slug",
    )
