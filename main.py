import user_input_utilities, request_utilities, data_parser, consts, schedule_utilities, users_utilities
from Database import Database
from DBQueries import DBQueries
import logging
from tasks import update_all_prices
from tasks import app


logging.basicConfig(filename='ksp_scraper.log', level=10
                    , format='%(asctime)s: %(module)s: %(funcName)s: %(levelname)s: %(message)s')

logger = logging.getLogger(__name__)


def connect_to_db():
    database = Database(consts)
    database.connect()
    database._db_setup()
    return database

#
# def update_all_prices():
#     db = connect_to_db()
#     db_queries = DBQueries(db)
#     list_of_items = db_queries.select_all_uin()
#     for uin in list_of_items:
#         text = request_utilities.get_text_from_url(consts.URL_TO_ADD_UIN + uin[1])
#         title_and_price = data_parser.get_title_and_price(text)
#         price = data_parser.change_price_from_str_to_decimal(title_and_price[1])
#         item_id = uin[0]
#         db_queries.add_price(item_id, price)


def check_for_decreasement_in_price():
    pass


def check_for_target_prices():
    pass



db = connect_to_db()
dbq = DBQueries(db)


if __name__ == '__main__':

    # user_id = 0
    # url = user_input_utilities.input_link()
    # uin = data_parser.parse_uin_from_url(url)
    # text = request_utilities.get_text_from_url(consts.URL_TO_ADD_UIN + uin)
    # title_and_price = data_parser.get_title_and_price(text)
    # price = data_parser.change_price_from_str_to_decimal(title_and_price[1])
    # title = title_and_price[0]
    # item_id = db_queries.add_item(title, uin, price)
    # db_queries.add_price(item_id, price)
    # db_queries.add_user_item(user_id, item_id, target_price=165)

    # schedule_utilities.schedule_timer(20, update_all_prices)

    # dbq.add_user('walla@walla.com', '123456')
    # dbq.add_user('gmail@gmail.com', '123456')
    #add user then add def login def signup

    # logged_user = users_utilities.user_login()
    # current_user_id = logged_user[0]
    # current_user_email = logged_user[1]
    # url = user_input_utilities.input_link()
    # uin = data_parser.parse_uin_from_url(url)
    # text = request_utilities.get_text_from_url(consts.URL_TO_ADD_UIN + uin)
    # title_and_price = data_parser.get_title_and_price(text)
    # price = data_parser.change_price_from_str_to_decimal(title_and_price[1])
    # print(f'Current price is:{price}.')
    # current_user_target_price = user_input_utilities.input_target_price()
    # title = title_and_price[0]
    # item_id = dbq.add_item(title, uin, price)
    # dbq.add_price(item_id, price)
    # dbq.add_user_item(current_user_id, item_id, current_user_target_price)

    update_all_prices.delay()
    #
    # list_of_items = dbq.select_all_uin()
    # def get_prices_list_from_uin_list(list_of_items):
    #     list_to_return = []
    #     for uin in list_of_items:
    #         text = request_utilities.get_text_from_url(consts.URL_TO_ADD_UIN + uin[1])
    #         title_and_price = data_parser.get_title_and_price(text)
    #         price = data_parser.change_price_from_str_to_decimal(title_and_price[1])
    #         item_id = uin[0]
    #         list_to_return.append((item_id, price))
    #     return list_to_return

    # list_of_items = dbq.select_all_uin()
    # new_list_of_items = []
    # for uin in list_of_items:
    #     text = request_utilities.get_text_from_url(consts.URL_TO_ADD_UIN + uin[1])
    #     title_and_price = data_parser.get_title_and_price(text)
    #     price = data_parser.change_price_from_str_to_decimal(title_and_price[1])
    #     item_id = uin[0]
    #     new_list_of_items.append((item_id, price))

    # dbq.check_for_lowest_price_and_update()

    # list_ = get_prices_list_from_uin_list(list_of_items)
    # print(list_)
    # dbq.check_for_lowest_price(list_)

    # list_of_id_and_prices = get_prices_list_from_uin_list(list_of_items)
    # dbq.add_prices(list_of_id_and_prices)


    pass