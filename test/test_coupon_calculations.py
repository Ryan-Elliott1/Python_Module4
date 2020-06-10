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

    def test_price_under_ten_to_thirty1(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(22, 5, .1), 24.64)

    def test_price_under_ten_to_thirty2(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(22, 5, .15), 23.74)

    def test_price_under_ten_to_thirty3(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(22, 5, .2), 22.84)

    def test_price_under_ten_to_thirty4(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(22, 10, .1), 19.88)

    def test_price_under_ten_to_thirty5(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(22, 10, .15), 19.24)

    def test_price_under_ten_to_thirty6(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(22, 10, .2), 18.60)


if __name__ == '__main__':
    unittest.main()
