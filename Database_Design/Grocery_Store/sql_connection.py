# connection details to mysql database
import mysql.connector


# creates a global variable so the connection only makes one connection when called
__cnx = None


def get_sql_connection():
    # global connection
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='trublue6',
                              host='127.0.0.1',
                              database='grocery_store')

    return __cnx
