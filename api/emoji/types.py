import datetime
import strawberry
import typing
import uuid


@strawberry.type
class Emoji:
    """
    A GraphQL type representing the Emoji model.
    """

    id: strawberry.ID
    uuid: uuid.UUID
    emoji: str
    name: str
    slug: typing.Optional[str] = None
    created_at: typing.Optional[datetime.datetime] = None
    updated_at: typing.Optional[datetime.datetime] = None
