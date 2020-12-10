import consts, request_utilities, data_parser, db_config, db_connection
from UserUtilities import UserUtilities
from celery import Celery
import logging
import time
from db_connection import dbq

app = Celery()
app.config_from_object('celery_config')
logger = logging.getLogger(__name__)


@app.task
def update_all_prices():
    db_connection.return_dbq()
    user_utilities = UserUtilities(dbq)
    list_of_items = dbq.select_all_uin()
    new_list_of_items = []
    logger.debug(f'List of uin to check: {new_list_of_items}.')
    for uin in list_of_items:
        logger.debug(f'The url is: {consts.URL_TO_ADD_UIN}{uin[1]}.')
        text = request_utilities.get_text_from_url(consts.URL_TO_ADD_UIN + uin[1])
        try:
            title_and_price = data_parser.get_title_and_price(text)
            if title_and_price:
                logger.debug(f'Title and price are: {title_and_price}.')
                price = data_parser.change_price_from_str_to_decimal(title_and_price[1])
                item_id = uin[0]
                new_list_of_items.append((item_id, price))
            else:
                dbq.change_to_out_of_stock(uin[1])
                user_utilities.notify_out_of_stock(dbq.check_users_for_out_of_stock_item(uin[0]))
        except:
            print(consts.GENERIC_ERROR_MESSAGE)

    dbq.add_prices(new_list_of_items)
    dbq.check_for_lowest_price_and_update()
    # todo check if there is a way to remove from this function:
    id_list_to_pass = [(item[0],) for item in new_list_of_items]
    logger.debug(f'{id_list_to_pass}')
    target_price_list = dbq.check_target_prices(tuple(id_list_to_pass))
    if target_price_list:
        logger.debug(f'Sleeping for 20 seconds.')
        time.sleep(20)
        logger.debug(f'Running notify_target_price')
        logger.debug(f'target price list: {target_price_list}')
        # todo check why I need the None
        user_utilities.notify_target_price(target_price_list)
    return new_list_of_items
