from Database import Database
from DBQueries import DBQueries
import consts,request_utilities,data_parser
from celery import Celery

app = Celery()
app.config_from_object('celery_config')

def connect_to_db():
    database = Database(consts)
    database.connect()
    database._db_setup()
    return database

@app.task
def update_all_prices():
    db = connect_to_db()
    db_queries = DBQueries(db)
    list_of_items = db_queries.select_all_uin()
    for uin in list_of_items:
        text = request_utilities.get_text_from_url(consts.URL_TO_ADD_UIN + uin[1])
        title_and_price = data_parser.get_title_and_price(text)
        price = data_parser.change_price_from_str_to_decimal(title_and_price[1])
        item_id = uin[0]
        db_queries.add_price(item_id, price)