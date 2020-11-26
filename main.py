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

# testing add item
item_uin = "37068"
item_link = consts.URL_TO_ADD_UIN+item_uin
def add_item(item_link):
    source_text_beautiful = request_utilities.get_text_from_url(item_link)
    title_and_price = data_parser.get_title_and_price(source_text_beautiful)
    if title_and_price:
        price = data_parser.change_price_from_str_to_decimal(title_and_price[1])
        print(dbq.add_item(title_and_price[0], item_uin))
    else:
        print(f'{consts.ITEM_OUT_OF_STOCK_MESSAGE}')

if __name__ == '__main__':
    # update_all_prices()
    add_item(item_link)