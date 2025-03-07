from django.shortcuts import get_object_or_404
from graphql import GraphQLResolveInfo
from .models import UserProfile
from .types import UserProfileType

def resolve_user_profile(parent, info: GraphQLResolveInfo, user_id: int):
    user_profile = get_object_or_404(UserProfile, id=user_id)
    return UserProfileType(id=user_profile.id, name=user_profile.name, bio=user_profile.bio)