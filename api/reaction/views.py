from rest_framework import generics, permissions

from .models import Reaction
from .serializers import ReactionSerializer

from core.utils import final_success_response


class ReactionCreateView(generics.CreateAPIView):
    """
    A generic view that creates a new object in the Reaction model.

    NOTE: Only a POST request.
    """

    permission_classes = (permissions.AllowAny,)
    queryset = Reaction.objects.all().order_by("reaction_count")
    serializer_class = ReactionSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        final_success_response(request, response)

        return super().finalize_response(request, response, *args, **kwargs)
