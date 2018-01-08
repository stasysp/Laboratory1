from execute import execute


import unittest

class ParsingTestSuite(unittest.TestCase):

    def test_parse_primitives(self):
        self.assertEqual(execute("1 2 *"), 2)
        self.assertEqual(execute("5 2 /"), 2)
        self.assertEqual(execute("5.0 2 /"), 2.5, 0.0001)
        self.assertEqual(execute("1 2 +"), 3)
        self.assertEqual(execute("1 2 -"), -1)

    def test_priority(self):
        self.assertEqual(execute("3 1 2 * +"), 5)
        self.assertEqual(execute("2 3 2 / -"), 1)
        self.assertEqual(execute("3 1 2 + *"), 9)
        self.assertEqual(execute("2 3 2 - /"), 2)

    def test_floating_points_operators(self):
        self.assertEqual(execute("3 1 2.5 * +"), 5.5, 0.0001)
        self.assertEqual(execute("2 3.0 2 / -"), 0.5, 0.0001)
        self.assertEqual(execute("2.5 3 2 - /"), 2.5, 0.0001)

    def test_intermediate_digits(self):
        self.assertEqual(execute("3 2 / 3 2 / -"), 0)
        self.assertEqual(execute("30 3 2 2 * + 2 / - 2 +"), 29)

    def test_intermediate_fp_digits(self):
        self.assertEqual(execute("30 3 2 2.0 * + 2 / - 2 +"), 28.5, 0.0001)
        self.assertEqual(execute("30.0 3.2 0.2 2.7 * + 2.1 / - 0.2 +"),
                         28.419047619047618, 0.000000000000001)
        self.assertEqual(execute("3.0 2 / 3 2 / -"), 0.5, 0.0001)

if __name__ == '__main__':
    unittest.main()


