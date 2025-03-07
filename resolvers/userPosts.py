from graphene import ObjectType, String, Int, Field, Schema, Mutation, List
from myapp.models import User, Post

class UserType(ObjectType):
    id = Int()
    username = String()
    email = String()
    posts = List(lambda: PostType)

class PostType(ObjectType):
    id = Int()
    title = String()
    content = String()
    author = Field(UserType)

class Query(ObjectType):
    users = List(UserType)
    posts = List(PostType)

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_posts(self, info):
        return Post.objects.select_related('author').all()

class CreateUser(Mutation):
    class Arguments:
        username = String(required=True)
        email = String(required=True)

    user = Field(UserType)

    def mutate(self, info, username, email):
        user = User(username=username, email=email)
        user.save()
        return CreateUser(user=user)

class CreatePost(Mutation):
    class Arguments:
        title = String(required=True)
        content = String(required=True)
        author_id = Int(required=True)

    post = Field(PostType)

    def mutate(self, info, title, content, author_id):
        author = User.objects.get(id=author_id)
        post = Post(title=title, content=content, author=author)
        post.save()
        return CreatePost(post=post)

class Mutation(ObjectType):
    create_user = CreateUser.Field()
    create_post = CreatePost.Field()

schema = Schema(query=Query, mutation=Mutation)