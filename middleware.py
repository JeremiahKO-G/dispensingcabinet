import sqlite3
from ctypes.wintypes import HCURSOR
from enum import nonmember


def authenticate(username, pswd):
    # connect the database
    connection = sqlite3.connect('wlcnursing.db')
    cursor = connection.cursor()

    cursor.execute(
        "SELECT ID, username, password, inserted_on, last_login"
        "FROM user"
        "WHERE username = ? and password = ?", (username, pswd)
    )

    user_info = cursor.fetchone()
    connection.close()

    if user_info is None:
        return None

    ID, username, password, inserted_on, last_login = user_info
    