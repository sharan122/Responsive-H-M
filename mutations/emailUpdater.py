def update_user_email(user_id, new_email):
    user = User.query.get(user_id)
    if user:
        user.email = new_email
        db.session.commit()
        return {'success': True, 'message': 'Email updated successfully.'}
    return {'success': False, 'message': 'User not found.'}