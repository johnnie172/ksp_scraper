import unittest
import data_parser
from decimal import Decimal
from bs4 import BeautifulSoup


class TestDataParser(unittest.TestCase):

    def test_get_title_and_price(self):
        with open('source_text.txt') as source_text:
            source_text_beautiful = BeautifulSoup(source_text, 'lxml')
            self.assertEqual(data_parser.get_title_and_price(source_text_beautiful),
                             ("עכבר גיימרים Corsair HARPOON RGB PRO FPS/MOBA", "165 ₪"))

    def test_change_price_from_str_to_decimal(self):
        self.assertEqual(data_parser.change_price_from_str_to_decimal("10.1"), Decimal("10.1"))
        self.assertEqual(data_parser.change_price_from_str_to_decimal("160 $"), Decimal("160"))
        self.assertEqual(data_parser.change_price_from_str_to_decimal("10.1 ₪"), Decimal("10.1"))
