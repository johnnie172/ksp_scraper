import user_input_utilities, request_utilities, data_parser, consts
from Database import Database
from DBQueries import DBQueries
import logging

logging.basicConfig(filename='ksp_scraper.log', level=10
                    , format='%(asctime)s: %(module)s: %(funcName)s: %(levelname)s: %(message)s')

logger = logging.getLogger(__name__)


if __name__ == '__main__':
    # id = data_parser.parse_uin_from_url('https://ksp.co.il/?uin=68851')
    # print(id)
    user_id = 0
    url = user_input_utilities.input_link()
    uin = data_parser.parse_uin_from_url(url)
    text = request_utilities.get_text_from_url(consts.URL_TO_ADD_UIN + uin)
    title_and_price = data_parser.get_title_and_price(text)
    price = data_parser.change_price_from_str_to_decimal(title_and_price[1])
    title = title_and_price[0]
    database = Database(consts)
    database.connect()
    database._db_setup()
    db_queries = DBQueries(database)
    item_id = db_queries.add_item(title, uin, price)
    db_queries.add_price(item_id, price)
    db_queries.add_user_item(user_id, item_id, target_price=165)

    pass