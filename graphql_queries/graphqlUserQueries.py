import gql
from typing import List, Any
from requests import Session

class GraphQLClient:
    def __init__(self, endpoint: str):
        self.session = Session()
        self.endpoint = endpoint

    def execute(self, query: str, variables: dict = None) -> Any:
        response = self.session.post(
            self.endpoint,
            json={'query': query, 'variables': variables},
            headers={'Content-Type': 'application/json'}
        )
        response.raise_for_status()
        return response.json()

class UserQueries:
    def __init__(self, client: GraphQLClient):
        self.client = client

    def get_users(self, limit: int = 10) -> List[dict]:
        query = gql("""
        query GetUsers($limit: Int) {
            users(limit: $limit) {
                id
                name
                email
            }
        }
        """)
        variables = {'limit': limit}
        result = self.client.execute(query, variables)
        return result['data']['users']

    def get_user_by_id(self, user_id: str) -> dict:
        query = gql("""
        query GetUserById($id: ID!) {
            user(id: $id) {
                id
                name
                email
            }
        }
        """)
        variables = {'id': user_id}
        result = self.client.execute(query, variables)
        return result['data']['user']

def create_client() -> GraphQLClient:
    endpoint = "https://api.example.com/graphql"
    return GraphQLClient(endpoint)

client = create_client()
user_queries = UserQueries(client)

users = user_queries.get_users()
user = user_queries.get_user_by_id('1')