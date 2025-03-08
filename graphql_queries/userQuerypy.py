from graphene import ObjectType, String, Schema, Field
from graphql import graphql_sync

class User(ObjectType):
    id = String()
    name = String()

class Query(ObjectType):
    user = Field(User, id=String(required=True))

    def resolve_user(self, info, id):
        # Simulated database lookup
        users = {'1': 'Alice', '2': 'Bob'}
        if id in users:
            return User(id=id, name=users[id])
        return None

schema = Schema(query=Query)

def execute_query(query_string):
    return graphql_sync(schema, query_string)

# Example usage
result = execute_query('{ user(id: "1") { id name } }')
print(result)