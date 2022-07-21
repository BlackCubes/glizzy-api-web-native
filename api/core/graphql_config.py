import strawberry

from glizzy.schema import Query as GlizzyQuery


schema = strawberry.Schema(query=GlizzyQuery)
