import strawberry
import typing

from . import types, resolvers


@strawberry.type
class Query:
    """
    A GraphQL schema that will execute a query of ``emojis`` which returns a
    list of zero or more emojis.
    """

    emojis: typing.List[types.Emoji] = strawberry.field(
        resolver=resolvers.get_emojis,
        description="Execute query of ``emojis`` that will return a list of zero or more emojis.",
    )
