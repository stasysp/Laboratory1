from parse import parse

import unittest

class ParsingTestSuite(unittest.TestCase):

    def test_parse_primitives(self):
        self.assertEqual(parse("1 * 2"), "1 2 *")
        self.assertEqual(parse("1 + 2"), "1 2 +")
        self.assertEqual(parse("1 / 2"), "1 2 /")
        self.assertEqual(parse("1 - 2"), "1 2 -")

    def test_priority(self):
        self.assertEqual(parse("3 + 1 * 2"), "3 1 2 * +")
        self.assertEqual(parse("2 - 3 / 2"), "2 3 2 / -")

    def test_braces(self):
        self.assertEqual(parse("20 / ( 5 + 3 )"), "20 5 3 + /")
        self.assertEqual(parse("30 - ( 3 + 2 ) / 2"), "30 3 2 + 2 / -")

    def test_long_braces(self):
        self.assertEqual(parse("30 - ( 3 + 2 * 2 ) / 2 + 2"),
                         "30 3 2 2 * + 2 / - 2 +")

    def test_floating_point_digits(self):
        self.assertEqual(parse("30. - ( 3.2 + 0.2 * 2.7 ) / 2.1 + .2"),
                         "30.0 3.2 0.2 2.7 * + 2.1 / - 0.2 +")

    def test_combining_dogots(self):
        self.assertEqual(parse("3.0 / 2 - 3 / 2"), "3.0 2 / 3 2 / -")


if __name__ == '__main__':
    unittest.main()


