from bs4 import BeautifulSoup
import requests
import logging

logger = logging.getLogger(__name__)


def get_text_from_url(item_link):
    source_text = requests.get('{}'.format(item_link)).text
    logger.info(f'The source text is: {source_text}')
    source_text_beautiful = BeautifulSoup(source_text, 'lxml')
    return source_text_beautiful
