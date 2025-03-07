import graphene
from graphene import ObjectType, String, Int, List, Field, Mutation, Schema
from typing import List as TypingList

class User(ObjectType):
    id = Int()
    name = String()
    email = String()

class UserInput(graphene.InputObjectType):
    name = String(required=True)
    email = String(required=True)

class Query(ObjectType):
    users = List(User)

    def resolve_users(self, info) -> TypingList[User]:
        return [
            User(id=1, name="Alice", email="alice@example.com"),
            User(id=2, name="Bob", email="bob@example.com"),
        ]

class CreateUser(Mutation):
    class Arguments:
        user_data = UserInput(required=True)

    user = Field(User)

    def mutate(self, info, user_data: UserInput) -> 'CreateUser':
        user = User(id=3, name=user_data.name, email=user_data.email)
        return CreateUser(user=user)

class Mutation(ObjectType):
    create_user = CreateUser.Field()

schema = Schema(query=Query, mutation=Mutation)