import datetime
import strawberry
import typing
import uuid


@strawberry.type(
    description="A base level type without the ``glizzy`` field. Also being shared when mutating ``Reaction`` which has the ``glizzy`` field."
)
class BaseReaction:
    """
    A GraphQL type representing most of the fields in the Reaction model
    except for the ``glizzy`` field. This is because this type is being shared
    in the ``reaction`` and ``glizzy`` apps. The ``reaction`` app needs the
    ``glizzy`` field to be displayed while the ``glizzy`` app does not (to
    avoid redundancy).
    """

    id: strawberry.ID
    uuid: uuid.UUID
    reaction_count: int
    emoji: str
    created_at: typing.Optional[datetime.datetime]
    updated_at: typing.Optional[datetime.datetime]


@strawberry.type(
    description="A ``Reaction`` type implementing ``BaseReaction`` (``BaseReaction`` is being used when querying ``Glizzy``). After mutation, all the fields from ``BaseReaction`` gets returned with the ``glizzy`` field from ``Reaction`` (``BaseReaction`` does not have the ``glizzy`` field)."
)
class Reaction(BaseReaction):
    """
    A GraphQL type representing the Reaction model with the ``glizzy`` field.
    """

    glizzy: str
