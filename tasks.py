from Database import Database
from DBQueries import DBQueries
import consts, request_utilities, data_parser, db_config
from celery import Celery
# from celery.utils.log import get_task_logger
import logging



app = Celery()
app.config_from_object('celery_config')


# logger = get_task_logger(__name__)
logger = logging.getLogger(__name__)

def connect_to_db():
    database = Database(db_config)
    database.connect()
    database._db_setup()
    return database


@app.task
def update_all_prices():
    db = connect_to_db()
    db_queries = DBQueries(db)
    list_of_items = db_queries.select_all_uin()
    new_list_of_items = []
    logger.debug(f'list of uin to check: {new_list_of_items}.')
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
                db_queries.change_in_stock(uin[1])
            #todo if item out of stock do somthing to db
        except:
            pass
    db_queries.add_prices(new_list_of_items)
    db_queries.check_for_lowest_price_and_update()