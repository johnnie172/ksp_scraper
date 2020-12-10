from DataBase import DataBase
from DBQueries import DBQueries
import db_config

db = None
dbq = None

def connect_to_db():
    database = DataBase(db_config)
    database.connect()
    database._db_setup()
    return database

def return_dbq():
    db = connect_to_db()
    global dbq
    dbq = DBQueries(db)

class DBConnection:
    pass