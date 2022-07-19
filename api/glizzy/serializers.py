from rest_framework import serializers

from .models import Glizzy

from reaction.serializers import ReactionSerializer


class GlizzySerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that maps all of the Glizzy model fields with the given
    serializer fields of ``id``, ``uuid``, ``name``, ``slug``, ``short_info``,
    ``long_info``, ``image``, ``reactions``, ``created_at``, and
    ``updated_at``.

    NOTE: All Django models have an ``id`` field by default upon creation.
    """

    reactions = ReactionSerializer(many=True, read_only=True)

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
            "reactions",
            "created_at",
            "updated_at",
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation["shortInfo"] = representation["short_info"]
        representation["longInfo"] = representation["long_info"]
        representation["createdAt"] = representation["created_at"]
        representation["updatedAt"] = representation["updated_at"]

        representation.pop("short_info")
        representation.pop("long_info")
        representation.pop("created_at")
        representation.pop("updated_at")

        if representation.get("reactions", None):
            for reaction in representation["reactions"]:
                reaction.pop("glizzy")
                reaction.pop("createdAt")
                reaction.pop("updatedAt")

        return representation
