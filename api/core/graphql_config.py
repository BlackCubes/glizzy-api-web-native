import strawberry
from strawberry.tools import merge_types

from emoji.schema import Query as EmojiQuery
from glizzy.schema import Query as GlizzyQuery


Query = merge_types(
    name="EmojiGlizzyReactionQueries", types=(EmojiQuery, GlizzyQuery)
)

schema = strawberry.Schema(query=Query)
