import strawberry
import typing

from . import types, resolvers


@strawberry.type
class Query:
    """
    A GraphQL schema that will execute queries of ``glizzys`` that will return
    a list of zero or more glizzys, and ``glizzy`` that will return one glizzy
    or none.
    """

    glizzys: typing.List[types.Glizzy] = strawberry.field(
        resolver=resolvers.get_glizzys,
        description="Execute query of ``glizzys`` that will return a list of zero or more glizzys.",
    )

    glizzy: typing.Optional[types.Glizzy] = strawberry.field(
        resolver=resolvers.get_glizzy,
        description="Execute query of ``glizzy`` that will return one glizzy or none. Can either use arguments of ``id``, ``slug``, or ``both``, but if no arguments are provided then an error occurs.",
    )
