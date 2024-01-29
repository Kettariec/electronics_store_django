def check_user(user, author):
    custom_perms = (
        'catalog.set_is_published'
    )
    if user == author or user.is_superuser is True:
        return True
    elif user.groups.filter(name='manager').exists() and user.has_perms(custom_perms):
        return True
    return False
