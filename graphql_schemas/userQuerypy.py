from graphene import ObjectType, String, Schema, Field

class User(ObjectType):
    id = String()
    name = String()
    email = String()

class Query(ObjectType):
    user = Field(User, id=String(required=True))

    def resolve_user(self, info, id):
        # Simulating a user lookup
        return User(id=id, name='John Doe', email='john@example.com')

schema = Schema(query=Query)