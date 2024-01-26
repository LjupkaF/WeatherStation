import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """create a database connection to SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object"""
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

if __name__ == '__main__':
    # r means passing raw string
    create_connection(r"/home/ljupka/Development/WeatherStation/weather.db")