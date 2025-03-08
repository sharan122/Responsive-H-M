import graphene

class UserType(graphene.ObjectType):
    id = graphene.ID(required=True)
    username = graphene.String(required=True)
    email = graphene.String(required=True)

class Query(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.ID(required=True))

    def resolve_user(self, info, id):
        # Simulate a database lookup
        users = {
            '1': {'id': '1', 'username': 'john_doe', 'email': 'john@example.com'},
            '2': {'id': '2', 'username': 'jane_doe', 'email': 'jane@example.com'}
        }
        return users.get(id)

schema = graphene.Schema(query=Query)