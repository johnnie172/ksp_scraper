import user_input_utilities, request_utilities, data_parser,\
    consts, db_config, schedule_utilities, users_utilities
from Database import Database
from DBQueries import DBQueries
import logging
from tasks import update_all_prices

logging.basicConfig(filename='ksp_scraper.log', level=10
                    , format='%(asctime)s: %(module)s: %(funcName)s: %(levelname)s: %(message)s')

logger = logging.getLogger(__name__)


def connect_to_db():
    database = Database(db_config)
    database.connect()
    database._db_setup()
    return database


db = connect_to_db()
dbq = DBQueries(db)

if __name__ == '__main__':
    update_all_prices.delay()
