"""For testing the calculator module"""

import unittest

import calc  # Module to be tested


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(2, -3), -1)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(0, 0), 0)

    def test_div(self):
        self.assertEqual(calc.div(10, 5), 2)
        self.assertAlmostEqual(calc.div(4, 3), 1.33, places=2)
        self.assertEqual(calc.div(0, 1), 0)
        with self.assertRaises(ZeroDivisionError):
            calc.div(10, 0)


if __name__ == "__main__":
    unittest.main()
