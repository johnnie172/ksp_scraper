import unittest
from unittest import mock
import user_input_utilities
import consts


class TestUserInputUtilities(unittest.TestCase):

    def test_input_link(self):
        with mock.patch('builtins.input', return_value="https://ksp.co.il/?ref=mobileToDesktop&uin=68851"):
            self.assertEqual(user_input_utilities.input_link(), "https://ksp.co.il/?ref=mobileToDesktop&uin=68851")

        with mock.patch('builtins.input', return_value="www.ksp.co.il/?ref=mobileToDesktop&uin=68851"):
            with self.assertRaisesRegex(Exception, consts.LINK_ERROR_MESSAGE):
                user_input_utilities.input_link()

    def test_input_target_price(self):
        with mock.patch('builtins.input', return_value="10"):
            self.assertEqual(user_input_utilities.input_target_price(), 10)

        with self.assertRaises(Exception):
            with mock.patch('builtins.input', return_value="10.4"):
                user_input_utilities.input_target_price()

        with self.assertRaises(Exception):
            with mock.patch('builtins.input', return_value="tdcc"):
                user_input_utilities.input_target_price()
