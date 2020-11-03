import psycopg2
from psycopg2.extras import DictCursor
import consts
import logging

logger = logging.getLogger(__name__)


class Database:
    """PostgreSQL Database class."""

    # todo change for params
    def __init__(self, consts):
        self.host = consts.DATABASE_HOST
        self.username = consts.DATABASE_USERNAME
        self.password = consts.DATABASE_PASSWORD
        self.port = consts.DATABASE_PORT
        self.dbname = consts.DATABASE_NAME
        self.conn = None

    def _db_setup(self):
        """Set up the postgres database."""
        self.get_connection()
        sql_file = open(consts.DATABASE_TABLES_SETUP_FILE, 'r')
        with self.conn.cursor() as cur:
            cur.execute(sql_file.read())
            self.conn.commit()
        logger.info(f'The script {consts.DATABASE_TABLES_SETUP_FILE} has run.')

    def connect(self):
        """Connect to a Postgres database."""
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                port=self.port,
                dbname=self.dbname
            )
        except psycopg2.DatabaseError as e:
            logger.error(e)
            raise e
        logger.info('Connection opened successfully.')

    def get_connection(self):
        """Returning connection item if None is exist"""
        if self.conn.closed != 0:
            self.connect()
        logger.debug(f'The connection object is: {self.conn}.')
        return self.conn

    def select_rows(self, query):
        """Run a SQL query to select rows from table."""
        self.get_connection()
        with self.conn.cursor() as cur:
            cur.execute(query)
            records = [row for row in cur.fetchall()]
            return records

    def select_rows_dict_cursor(self, query):
        """Run SELECT query and return list of dicts."""
        self.get_connection()
        with self.conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(query)
            records = cur.fetchall()
            return records

    def _update_rows(self, query):
        """Run a SQL query to update rows in table."""
        self.get_connection()
        with self.conn.cursor() as cur:
            cur.execute(query)
            self.conn.commit()
            logger.info(f"{cur.rowcount} rows affected.")

    def _insert_into_table(self, query, vars):
        """Run a SQL query to insert rows in table."""
        self.get_connection()
        with self.conn.cursor() as cur:
            cur.execute(query, vars)
            self.conn.commit()
            logger.info(f"{cur.rowcount} rows affected.")

    def add_user(self, user_email, user_password):
        """Run a INSERT query to insert new user"""
        # getting 2 values(email, password) and forming them into a tuple.
        vars = (user_email, user_password)
        insert_command = "INSERT INTO users (email, password) VALUES (%s, %s)"
        self._insert_into_table(insert_command, vars)
        logger.debug(f'Query is: {insert_command}, the vars are{vars}.')

    def add_item(self, item_title, item_price, lowest_price):
        """Run a INSERT query to insert new item"""
        # getting 3 values(title, price, lowest) and forming them into a tuple.
        vars = (item_title, item_price, lowest_price)
        insert_command = "INSERT INTO items (title, price, lowest) VALUES (%s, %s, %s)"
        self._insert_into_table(insert_command, vars)
        logger.debug(f'Query is: {insert_command}, the vars are{vars}.')

    def add_user_item(self, user_id, item_id, target_price):
        """Run a INSERT query to insert new item"""
        # getting 3 values(user_id, item_id, target_price) and forming them into a tuple.
        vars = (user_id, item_id, target_price)
        insert_command = "INSERT INTO items (title, price, lowest) VALUES (%s, %s, %s)"
        self._insert_into_table(insert_command, vars)
        logger.debug(f'Query is: {insert_command}, the vars are{vars}.')

    def add_price(self, item_id, item_price, timestamp):
        """Run a INSERT query to insert new item"""
        # getting 3 values(item_id, item_price, timestamp) and forming them into a tuple.
        vars = (item_id, item_price, timestamp)
        insert_command = "INSERT INTO items (title, price, lowest) VALUES (%s, %s, %s)"
        self._insert_into_table(insert_command, vars)
        logger.debug(f'Query is: {insert_command}, the vars are{vars}.')



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
