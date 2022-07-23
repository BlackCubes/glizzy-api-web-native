import strawberry
import typing

from . import resolvers, types


@strawberry.type
class Mutation:
    """
    A GraphQL schema that will execute mutation of ``add_reaction`` which
    returns a one reaction or none.
    """

    add_reaction: typing.Optional[types.Reaction] = strawberry.field(
        resolver=resolvers.add_reaction,
        description="Execute mutation of ``addReaction`` that will return one reaction or none. Must use arguments of ``emoji``, ``glizzy``, and ``reactionCount``. ``emoji`` must be the an actual emoji (i.e. 🌭), and the ``glizzy`` must be the name of the frank (i.e. 'Chicago Dog'). Errors will occur if the ``reactionCount`` is not 0 or greater; both the ``emoji`` and ``glizzy`` are empty strings; or both ``emoji`` and ``glizzy`` could not be found in the database.",
    )
