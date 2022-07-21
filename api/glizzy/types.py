import datetime
import strawberry
import typing
import uuid


@strawberry.type()
class Glizzy:
    """
    A GraphQL type representing the Glizzy model.
    """

    id: strawberry.ID
    uuid: uuid.UUID
    name: str
    short_info: str
    long_info: str
    slug: typing.Optional[str] = None
    image: typing.Optional[str] = None
    created_at: typing.Optional[datetime.datetime] = None
    updated_at: typing.Optional[datetime.datetime] = None
