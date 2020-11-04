from bs4 import BeautifulSoup
import requests
import logging

logger = logging.getLogger(__name__)


def get_text_from_url(item_link):
    """Function that request link and converting it into BeautifulSoup text."""
    source_text = requests.get('{}'.format(item_link)).text
    logger.info(f'Source text is been downloaded.')
    source_text_beautiful = BeautifulSoup(source_text, 'lxml')
    return source_text_beautiful
