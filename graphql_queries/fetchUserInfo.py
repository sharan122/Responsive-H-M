from graphql import GraphQLError

def resolve_user(parent, info, user_id):
    user = get_user_by_id(user_id)
    if not user:
        raise GraphQLError('User not found')
    return user

user_query = '''
    query getUser($userId: ID!) {
        user(id: $userId) {
            id
            name
            email
        }
    }
'''