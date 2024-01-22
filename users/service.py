def check_user(user, author):
    if user == author or user.is_superuser is True:
        return True
