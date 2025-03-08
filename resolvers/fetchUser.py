def get_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        return {'id': user.id, 'name': user.name, 'email': user.email}
    return None