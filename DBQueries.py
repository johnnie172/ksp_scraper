from Database import Database
import psycopg2
from psycopg2.extras import DictCursor
from psycopg2.errors import UniqueViolation
import logging

logger = logging.getLogger(__name__)


class DBQueries:

    def __init__(self, database):
        self.db = database

    """Run queries for DataBase"""

    def select_rows(self, query):
        """Run a SQL query to select rows from table."""
        self.db.get_connection()
        with self.db.conn.cursor() as cur:
            cur.execute(query)
            records = [row for row in cur.fetchall()]
            return records

    def select_rows_dict_cursor(self, query):
        """Run a SELECT query and return list of dicts."""
        self.db.get_connection()
        with self.db.conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(query)
            records = cur.fetchall()
            return records

    def _update_rows(self, query):
        """Run a SQL query to update rows in table."""
        self.db.get_connection()
        with self.db.conn.cursor() as cur:
            cur.execute(query)
            self.db.conn.commit()
            logger.info(f"{cur.rowcount} rows affected.")

    def _insert(self, query, vars):
        """Run a SQL query to insert rows in table."""
        self.db.get_connection()
        with self.db.conn.cursor() as cur:
            cur.execute(query, vars)
            self.db.conn.commit()
            logger.info(f"{cur.rowcount} rows affected.")

    def _insert_and_return_id(self, query, vars, select_id_command):
        """Run a SQL query to insert rows in table and return id."""
        self.db.get_connection()
        query = query + ' RETURNING id'
        with self.db.conn.cursor() as cur:
            try:
                cur.execute(query, vars)
                id = cur.fetchone()[0]
                self.db.conn.commit()
            except(UniqueViolation):
                logger.debug('There is UniqueViolation error preforming rollback and returning id')
                self.db.conn.rollback()
                cur.execute(select_id_command, (vars[0],))
                id = cur.fetchone()[0]
                self.db.conn.commit()
            logger.info(f"{cur.rowcount} rows affected, the id is:{id} ")
            return id

    def add_user(self, user_email, user_password):
        """Run an INSERT query to insert new user"""
        # getting 2 values(email, password) and forming them into a tuple.
        vars = (user_email, user_password)
        insert_command = "INSERT INTO users (email, password) VALUES (%s, %s)"
        select_id_command = "SELECT id FROM users WHERE email = %s"
        id = self._insert_and_return_id(insert_command, vars, select_id_command)
        logger.debug(f'Query is: {insert_command}, the vars are{vars}.')
        return id

    def add_item(self, item_title, item_uin, lowest=None):
        """Run an INSERT query to insert new item"""
        # getting 3 values(title, url, lowest) and forming them into a tuple.
        vars = (item_title, item_uin, lowest)
        insert_command = "INSERT INTO items (title, uin, lowest) VALUES (%s, %s, %s)"
        select_id_command = "SELECT id FROM items WHERE title = %s"
        id = self._insert_and_return_id(insert_command, vars, select_id_command)
        logger.debug(f'Query is: {insert_command}, the vars are{vars}.')
        return id

    def add_price(self, item_id, price):
        """Run an INSERT query to insert new price"""
        # getting 2 values(item_id, price) and forming them into a tuple auto add timestamp.
        vars = (item_id, price)
        insert_command = "INSERT INTO prices (item_id, price) VALUES (%s, %s)"
        self._insert(insert_command, vars)
        logger.debug(f'Query is: {insert_command}, the vars are{vars}.')

    def add_user_item(self, user_id, item_id, target_price):
        """Run an INSERT query to insert new user item"""
        # getting 3 values(user_id, item_id, target_price) and forming them into a tuple.
        vars = (user_id, item_id, target_price)
        insert_command = "INSERT INTO users_items (user_id, item_id, target_price) VALUES (%s, %s, %s)"
        self._insert(insert_command, vars)
        logger.debug(f'Query is: {insert_command}, the vars are{vars}.')
    #
    # def add_user_item(self, user_id, item_id, target_price):
    #     """Run a INSERT query to insert new item"""
    #     # getting 3 values(user_id, item_id, target_price) and forming them into a tuple.
    #     vars = (user_id, item_id, target_price)
    #     insert_command = "INSERT INTO items (title, price, lowest) VALUES (%s, %s, %s)"
    #     self._insert_into_table(insert_command, vars)
    #     logger.debug(f'Query is: {insert_command}, the vars are{vars}.')

    # def add_price(self, item_id, item_price):
    #     """Run a INSERT query to insert new item"""
    #     # getting 3 values(item_id, item_price, timestamp) and forming them into a tuple.
    #     vars = (item_id, item_price)
    #     insert_command = "INSERT INTO prices (title, price, lowest) VALUES (%s, %s, %s)"
    #     self._insert_into_table(insert_command, vars)
    #     logger.debug(f'Query is: {insert_command}, the vars are{vars}.')

# try:
#    conn = psycopg2.connect(
#          database=consts.DATABASE_NAME, user=consts.DATABASE_USERNAME, password=consts.DATABASE_PASSWORD,
#          host=consts.DATABASEHOST, port= consts.DATABASEPORT
#       )
#
#    cursor = conn.cursor()
# except psycopg2.DatabaseError as error:
#    logger.exception(error)
#    logger.info(f'Connected to {consts.DATABASE_NAME} as {consts.DATABASE_USER}.')
#
# def create_users_table():
#
#    #Creating table as per requirement
#    sql ='''CREATE TABLE IF NOT EXISTS users
#    (
#       id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#       email VARCHAR(320),
#       password varchar(30) NOT NULL
#    )'''
#    try:
#       cursor.execute(sql)
#
#       #Closing the connection
#       conn.commit()
#       cursor.close()
#    except psycopg2.DatabaseError as error:
#       logger.exception(error)
#
#    finally:
#       if conn is not None:
#          conn.close()
#          logger.info('users table created!')
#
# def show_usres_table():
#    try:
#
#       postgreSQL_select_Query = "select * from users"
#
#       cursor.execute(postgreSQL_select_Query)
#       print("Selecting rows from mobile table using cursor.fetchall")
#       mobile_records = cursor.fetchall()
#
#       print("Print each row and it's columns values")
#       for row in mobile_records:
#          print("Id = ", row[0], )
#          print("Email = ", row[1])
#          print("Password  = ", row[2], "\n")
#
#    except (Exception, psycopg2.Error) as error:
#       print("Error while fetching data from PostgreSQL", error)
#
#    finally:
#       # closing database connection.
#       if (connection):
#          cursor.close()
#          connection.close()
#          print("PostgreSQL connection is closed")
#

# example :
# import psycopg2
#
# cars = (
#     (1, 'Audi', 52642),
#     (2, 'Mercedes', 57127),
#     (3, 'Skoda', 9000),
#     (4, 'Volvo', 29000),
#     (5, 'Bentley', 350000),
#     (6, 'Citroen', 21000),
#     (7, 'Hummer', 41400),
#     (8, 'Volkswagen', 21600)
# )
#
# con = psycopg2.connect(database='testdb', user='postgres',
#                     password='s$cret')
#
# with con:
#
#     cur = con.cursor()
#
#     cur.execute("DROP TABLE IF EXISTS cars")
#     cur.execute("CREATE TABLE cars(id SERIAL PRIMARY KEY, name VARCHAR(255), price INT)")
#
#     query = "INSERT INTO cars (id, name, price) VALUES (%s, %s, %s)"
#     cur.executemany(query, cars)
#
#     con.commit()
