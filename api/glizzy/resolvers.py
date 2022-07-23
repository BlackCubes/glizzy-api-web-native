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

    # In order to output the reactions. This works since it creates a new
    # ``glizzys`` reference because of the ``DictionaryToClass``. Without it,
    # ``glizzy.reactions`` would always point to its ``RelatedManager`` making
    # it not an iterable queryset.
    # Example: ``glizzy.reactions`` -> related manager.
    # But, making it an iterable queryset: ``glizzy.reactions.all()``.
    glizzys = [
        DictionaryToClass(
            {
                "id": glizzy.id,
                "uuid": glizzy.uuid,
                "name": glizzy.name,
                "short_info": glizzy.short_info,
                "long_info": glizzy.long_info,
                "slug": glizzy.slug,
                "image": info.context.request.build_absolute_uri(
                    glizzy.image.url
                )
                if glizzy.image
                else None,
                "reactions": glizzy.reactions.select_related("emoji")
                .all()
                .order_by("reaction_count"),
                "created_at": glizzy.created_at,
                "updated_at": glizzy.updated_at,
            }
        )
        for glizzy in glizzys
    ]

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

    # In order to output the reactions. See the huge comment section above for
    # an explanation.
    glizzy = DictionaryToClass(
        {
            "id": glizzy.id,
            "uuid": glizzy.uuid,
            "name": glizzy.name,
            "short_info": glizzy.short_info,
            "long_info": glizzy.long_info,
            "slug": glizzy.slug,
            "image": glizzy.image,
            "reactions": glizzy.reactions.select_related("emoji")
            .all()
            .order_by("reaction_count"),
            "created_at": glizzy.created_at,
            "updated_at": glizzy.updated_at,
        }
    )

    return glizzy
