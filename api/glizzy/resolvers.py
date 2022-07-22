import strawberry
import typing

from . import models, types

from core.utils import DictionaryToClass


def get_glizzys(info: strawberry.types.Info) -> typing.List[types.Glizzy]:
    """
    A resolver that returns a list from the Glizzy model.
    """

    glizzys: typing.List[models.Glizzy] = models.Glizzy.objects.all().order_by(
        "name"
    )

    if len(glizzys):
        for glizzy in glizzys:
            glizzy.image = (
                info.context.request.build_absolute_uri(glizzy.image.url)
                if glizzy.image
                else None
            )

    return glizzys


def get_glizzy(
    info: strawberry.types.Info,
    id: typing.Optional[strawberry.ID] = None,
    slug: typing.Optional[str] = None,
) -> typing.Optional[types.Glizzy]:
    """
    A resolver that returns an object from the Glizzy model.

    If both the arguments of ``id`` and ``slug`` are not provided, then an
    ``Exception`` is raised.

    If the object cannot be found, then an ``Exception`` is raised.
    """

    if not id and not slug:
        raise Exception(
            "Field 'glizzy' of either arguments of 'id' of type 'ID' or 'slug' of type 'String' are required, but it was not provided."
        )

    field_filter = {}

    if id:
        field_filter["id"] = id

    if slug:
        field_filter["slug"] = slug

    try:
        glizzy: models.Glizzy = models.Glizzy.objects.prefetch_related(
            "reactions"
        ).get(**field_filter)
    except models.Glizzy.DoesNotExist:
        raise Exception("The glizzy does not exist.")

    glizzy.image = (
        info.context.request.build_absolute_uri(glizzy.image.url)
        if glizzy.image
        else None
    )

    glizzy = DictionaryToClass(
        {
            "id": glizzy.id,
            "uuid": glizzy.uuid,
            "name": glizzy.name,
            "short_info": glizzy.short_info,
            "long_info": glizzy.long_info,
            "slug": glizzy.slug,
            "image": glizzy.image,
            "reactions": glizzy.reactions.all()
            .select_related("emoji")
            .order_by("reaction_count"),
            "created_at": glizzy.created_at,
            "updated_at": glizzy.updated_at,
        }
    )

    return glizzy
