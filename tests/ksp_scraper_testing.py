import unittest
import tests.user_input_utilities_test
import tests.data_parser_test

def suite():

    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(tests.user_input_utilities_test.TestUserInputUtilities))
    test_suite.addTest(unittest.makeSuite(tests.data_parser_test.TestDataParser))

    return test_suite

mySuit=suite()

if __name__ == '__main__':
    runner=unittest.TextTestRunner()
    runner.run(mySuit)