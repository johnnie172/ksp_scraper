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

