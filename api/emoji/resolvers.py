import typing

from . import models, types


def get_emojis() -> typing.List[types.Emoji]:
    """
    A resolver that returns a list from the Emoji model.
    """

    emojis: typing.List[models.Emoji] = models.Emoji.objects.all().order_by(
        "name"
    )

    return emojis
