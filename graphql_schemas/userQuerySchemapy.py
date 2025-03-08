from graphene import ObjectType, String, Schema, Field

class User(ObjectType):
    id = String()
    name = String()
    email = String()

class Query(ObjectType):
    user = Field(User, id=String(required=True))

    def resolve_user(self, info, id):
        # Simulating a user fetch from a database
        users = {"1": {"id": "1", "name": "Alice", "email": "alice@example.com"},
                 "2": {"id": "2", "name": "Bob", "email": "bob@example.com"}} 
        return users.get(id, None)

schema = Schema(query=Query)