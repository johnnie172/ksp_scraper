import user_input_utilities, request_utilities, data_parser, consts
from Database import Database
from DBQueries import DBQueries
from bs4 import BeautifulSoup
import logging

logging.basicConfig(filename='ksp_scraper.log', level=10
                    , format='%(asctime)s: %(module)s: %(funcName)s: %(levelname)s: %(message)s')

logger = logging.getLogger(__name__)


if __name__ == '__main__':
    url = user_input_utilities.input_link()
    text = request_utilities.get_text_from_url(url)
    title_and_price = data_parser.get_title_and_price(text)
    price = data_parser.change_price_from_str_to_decimal(title_and_price[1])
    title = title_and_price[0]
    database = Database(consts)
    database.connect()
    database._db_setup()
    db_queries = DBQueries(database)
    print(db_queries.add_item(title, url, price))

    pass