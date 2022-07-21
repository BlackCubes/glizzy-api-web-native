import datetime
import strawberry
import typing
import uuid


@strawberry.type
class Reaction:
    """
    A GraphQL type representing the Reaction model.
    """

    id: strawberry.ID
    uuid: uuid.UUID
    reaction_count: int
    emoji: str
    glizzy: str
    created_at: typing.Optional[datetime.datetime] = None
    updated_at: typing.Optional[datetime.datetime] = None
