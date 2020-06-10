import unittest
from store import coupon_calculations


class FunctionTestCase(unittest.TestCase):
    def test_price_under_ten1(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(9, 5, .1), 9.77)

    def test_price_under_ten2(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(9, 5, .15), 9.55)

    def test_price_under_ten3(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(9, 5, .2), 9.34)

    def test_price_under_ten4(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(9, 10, .1), 4.92)

    def test_price_under_ten5(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(9, 10, .15), 4.87)

    def test_price_under_ten6(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(9, 10, .2), 4.82)


if __name__ == '__main__':
    unittest.main()
