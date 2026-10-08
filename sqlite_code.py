import sqlite3

def get_user(username, pswd):
    # connect the database
    connection = sqlite3.connect('wlcnursing.db')
    cursor = connection.cursor()

    # grab the tuple matching with given username and password
    cursor.execute(
        """SELECT ID, username, password, inserted_on, last_login
           FROM user
           WHERE username = ?
             and password = ?""", (username, pswd)
    )

    user_info = cursor.fetchone()
    connection.close()

    # if there is no tuple with matching username and password, return none
    if user_info is None:
        return None

    # return tuple data
    ID, username, password, inserted_on, last_login = user_info

    return {
        "ID": ID,
        "username": username,
        "password": password,
        "inserted_on": inserted_on,
        "last_login": last_login
    }