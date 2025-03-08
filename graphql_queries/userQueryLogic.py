from graphene import ObjectType, String, Field, Schema

class User(ObjectType):
    id = String()
    name = String()
    email = String()

class Query(ObjectType):
    user = Field(User, id=String(required=True))

    def resolve_user(self, info, id):
        return get_user_by_id(id)

schema = Schema(query=Query)