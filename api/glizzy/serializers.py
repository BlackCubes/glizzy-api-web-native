from rest_framework import serializers

from .models import Glizzy


class GlizzySerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that maps all of the Glizzy model fields with the given
    serializer fields of ``id``, ``uuid``, ``name``, ``slug``, ``short_info``,
    ``long_info``, ``image``, ``created_at``, and ``updated_at``.

    NOTE: All Django models have an ``id`` field by default upon creation.
    """

    class Meta:
        model = Glizzy
        fields = (
            "id",
            "uuid",
            "name",
            "slug",
            "short_info",
            "long_info",
            "image",
            "created_at",
            "updated_at",
        )
