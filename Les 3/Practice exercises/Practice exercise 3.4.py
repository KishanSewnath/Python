def new_password(newpassword, oldpassword):
    if len(newpassword) < 6:
        return False
    elif newpassword == oldpassword:
        return False

    else:
        return True
print(new_password('hfjdyf', 'hfjd '))
