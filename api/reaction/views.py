from rest_framework import generics, permissions

from .models import Reaction
from .serializers import ReactionSerializer

from core.utils import final_success_response


class ReactionListCreateView(generics.ListCreateAPIView):
    """
    A generic view that finds all objects from the Reaction model.

    NOTE: Only a GET and POST request.
    """

    permission_classes = (permissions.AllowAny,)
    queryset = Reaction.objects.all().order_by("reaction_count")
    serializer_class = ReactionSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        final_success_response(request, response)

        return super().finalize_response(request, response, *args, **kwargs)
