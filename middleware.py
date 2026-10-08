from sqlite_code import get_user

def authenticate(username, pswd):
    # grab the user info if it exists in the user table
    user = get_user(username, pswd)

    # check if the table contains the user associated with the pass
    if user is None:
        return False

    return True