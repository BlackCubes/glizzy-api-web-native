from rest_framework import serializers

from .models import Reaction
from .utils import model_error_messages

from emoji.models import Emoji

from glizzy.models import Glizzy


class ReactionSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that maps all of the Reaction model fields with the
    given serializer fields of ``id``, ``uuid``, ``reaction_count``,
    ``emoji``, ``glizzy``, ``created_at``, and ``updated_at``.

    NOTE: All Django models have an ``id`` field by defailt upon creation.
    """

    emoji = serializers.SlugRelatedField(
        slug_field="emoji",
        queryset=Emoji.objects.all(),
        error_messages=model_error_messages["emoji"],
    )
    glizzy = serializers.SlugRelatedField(
        slug_field="slug",
        queryset=Glizzy.objects.all(),
        error_messages=model_error_messages["glizzy"],
    )
    reaction_count = serializers.IntegerField(
        min_value=0, error_messages=model_error_messages["reaction_count"]
    )

    class Meta:
        model = Reaction
        fields = (
            "id",
            "uuid",
            "reaction_count",
            "emoji",
            "glizzy",
            "created_at",
            "updated_at",
        )

    def create(self, validated_data):
        incoming_emoji = self.initial_data.get("emoji", None)
        incoming_glizzy = self.initial_data.get("glizzy", None)

        if incoming_emoji is not None and incoming_glizzy is not None:
            try:
                update_reaction = Reaction.objects.get(
                    emoji__emoji=incoming_emoji, glizzy__slug=incoming_glizzy
                )
            except Reaction.DoesNotExist:
                pass
            else:
                update_reaction.reaction_count += validated_data[
                    "reaction_count"
                ]

                update_reaction.save()

                return update_reaction

        new_reaction = Reaction.objects.create(**validated_data)

        return new_reaction
