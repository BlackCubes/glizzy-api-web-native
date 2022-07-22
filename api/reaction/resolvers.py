from . import models, types
from .utils import model_error_messages

from core.utils import DictionaryToClass

import emoji.models as emoji_models

import glizzy.models as glizzy_models


def add_reaction(
    emoji: str, glizzy: str, reaction_count: int
) -> types.Reaction:
    """
    A resolver that mutates the Reaction model and returns its object.

    Checks on two cases: If the object exists, then it increments the
    ``reaction_count``. Otherwise, if the object does not exist, then it
    creates a new one.
    """

    validate_add_reaction(
        emoji=emoji, glizzy=glizzy, reaction_count=reaction_count
    )

    try:
        update_reaction: models.Reaction = models.Reaction.objects.get(
            emoji__emoji=emoji, glizzy__name=glizzy
        )
    except models.Reaction.DoesNotExist:
        pass
    else:
        update_reaction.reaction_count += reaction_count

        update_reaction.save()

        # This is done so that the ``emoji`` from the Emoji model and the
        # ``name`` from the Glizzy model could be outputted instead of the
        # foreign key instance.
        update_reaction = DictionaryToClass(
            {
                "id": update_reaction.id,
                "uuid": update_reaction.uuid,
                "reaction_count": update_reaction.reaction_count,
                "emoji": emoji,
                "glizzy": glizzy,
                "created_at": update_reaction.created_at,
                "updated_at": update_reaction.updated_at,
            }
        )

        return update_reaction

    new_reaction: models.Reaction = models.Reaction.objects.create(
        emoji=emoji, glizzy=glizzy, reaction_count=reaction_count
    )

    # So that the ``emoji`` and ``glizzy`` could be shown instead of its
    # foreign key instance.
    new_reaction = DictionaryToClass(
        {
            "id": new_reaction.id,
            "uuid": new_reaction.uuid,
            "reaction_count": new_reaction.reaction_count,
            "emoji": emoji,
            "glizzy": glizzy,
            "created_at": new_reaction.created_at,
            "updated_at": new_reaction.updated_at,
        }
    )

    return new_reaction


def validate_add_reaction(emoji: str, glizzy: str, reaction_count: int):
    """
    Validates the ``add_reaction`` resolver.
    """

    # Validations check
    if reaction_count <= -1:
        print("Hello!!")
        raise Exception(model_error_messages["reaction_count"]["min_value"])

    if not emoji:
        raise Exception(model_error_messages["emoji"]["blank"])

    if not glizzy:
        raise Exception(model_error_messages["glizzy"]["blank"])

    # Check if the models exist
    try:
        emoji_models.Emoji.objects.get(emoji=emoji)
    except emoji_models.Emoji.DoesNotExist:
        raise Exception(model_error_messages["emoji"]["does_not_exist"])

    try:
        glizzy_models.Glizzy.objects.get(name=glizzy)
    except glizzy_models.Glizzy.DoesNotExist:
        raise Exception(model_error_messages["glizzy"]["does_not_exist"])
