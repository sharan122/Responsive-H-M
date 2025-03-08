from graphql import GraphQLObjectType, GraphQLField, GraphQLString, GraphQLSchema

user_type = GraphQLObjectType(
    name='User',
    fields={
        'id': GraphQLField(GraphQLString),
        'name': GraphQLField(GraphQLString),
        'email': GraphQLField(GraphQLString),
    }
)

query_type = GraphQLObjectType(
    name='Query',
    fields={
        'user': GraphQLField(user_type, resolver=lambda obj, info: {'id': '1', 'name': 'John Doe', 'email': 'john@example.com'})
    }
)

schema = GraphQLSchema(query=query_type)