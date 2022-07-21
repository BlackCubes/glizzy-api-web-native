import strawberry
from strawberry.tools import merge_types

from emoji.schema import Query as EmojiQuery
from glizzy.schema import Query as GlizzyQuery
from reaction.schema import Mutation as ReactionMutation


Query = merge_types(
    name="EmojiGlizzyQueries",
    types=(EmojiQuery, GlizzyQuery),
)

Mutation = merge_types(
    name="ReactionMutation",
    types=(ReactionMutation,),
)

schema = strawberry.Schema(query=Query, mutation=Mutation)
