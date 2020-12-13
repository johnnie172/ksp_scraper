import db_connection
import orchestrator
from UserUtilities import UserUtilities
from celery import Celery
import logging

app = Celery()
app.config_from_object('celery_config')
logger = logging.getLogger(__name__)


@app.task
def celery_main_task():

    db_queries = db_connection.get_db_queries()
    user_utilities = UserUtilities(db_queries)
    items_list = orchestrator.get_items_data(db_queries=db_connection.get_db_queries())

    items_to_store = items_list[0]
    out_of_stock_items = items_list[1]

    orchestrator.out_of_stock_manger(db_queries=db_queries, user_utilities=user_utilities,
                                     out_of_stock_items=out_of_stock_items)
    target_price_list = orchestrator.storing_and_sorting_items_data(db_queries, items_to_store)
    user_utilities.notify_target_price(target_price_list)
























# @app.task
# def update_all_prices():
#     # Creating list of all users items
#     db_queries = db_connection.get_db_queries()
#     user_utilities = UserUtilities(db_queries)
#     list_of_items = db_queries.select_all_uin()
#     #todo changee logics to 1. getting all the data
#     # 2. spliting the data items in and out of stock
#     # 3. storing and notify
#     # Creating new module and make functions instead of update all prices!!!
#
#     # Getting title and price for all item
#     new_list_of_items = []
#     logger.debug(f'List of uin to check: {new_list_of_items}.')
#     for uin in list_of_items:
#         logger.debug(f'The url is: {consts.URL_TO_ADD_UIN}{uin[1]}.')
#         text = request_utilities.get_text_from_url(consts.URL_TO_ADD_UIN + uin[1])
#         try:
#             title_and_price = data_parser.get_title_and_price(text)
#             # Checking if item is in stock and storing the price or
#             if title_and_price:
#                 logger.debug(f'Title and price are: {title_and_price}.')
#                 price = data_parser.change_price_from_str_to_decimal(title_and_price[1])
#                 item_id = uin[0]
#                 new_list_of_items.append((item_id, price))
#             else:
#                 db_queries.change_to_out_of_stock(uin[1])
#                 user_utilities.notify_out_of_stock(db_queries.check_users_for_out_of_stock_item(uin[0]))
#         except:
#             print(consts.GENERIC_ERROR_MESSAGE)
#
#     db_queries.add_prices(new_list_of_items)
#     db_queries.check_for_lowest_price_and_update()
#     # todo check if there is a way to remove from this function:
#     id_list_to_pass = [(item[0],) for item in new_list_of_items]
#     logger.debug(f'{id_list_to_pass}')
#     target_price_list = db_queries.check_target_prices(tuple(id_list_to_pass))
#     if target_price_list:
#         logger.debug(f'Sleeping for 20 seconds.')
#         time.sleep(20)
#         logger.debug(f'Running notify_target_price')
#         logger.debug(f'target price list: {target_price_list}')
#         # todo check why I need the None
#         user_utilities.notify_target_price(target_price_list)
#     return new_list_of_items
