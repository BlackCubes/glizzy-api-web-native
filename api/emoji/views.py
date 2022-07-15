from rest_framework import generics, permissions

from .models import Emoji
from .serializers import EmojiSerializer

from core.utils import final_success_response


class EmojiListView(generics.ListAPIView):
    """
    A generic view that finds all objects from the Emoji model.

    NOTE: Only a GET request.
    """

    permission_classes = (permissions.AllowAny,)
    queryset = Emoji.objects.all().order_by("name")
    serializer_class = EmojiSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        final_success_response(request, response)

        return super().finalize_response(request, response, *args, **kwargs)
