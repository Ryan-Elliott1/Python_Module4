import unittest
from store import coupon_calculations


class FunctionTestCase(unittest.TestCase):
    def test_price_under_ten1(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(9, 5, .1), 10.12)

    def test_price_under_ten2(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(9, 5, .15), 9.91)

    def test_price_under_ten3(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(9, 5, .2), 9.70)

    def test_price_under_ten4(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(9, 10, .1), 5.35)

    def test_price_under_ten5(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(9, 10, .15), 5.41)

    def test_price_under_ten6(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(9, 10, .2), 5.46)


if __name__ == '__main__':
    unittest.main()
