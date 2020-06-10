import unittest
from store import coupon_calculations


class FunctionTestCase(unittest.TestCase):
    # Price under $10
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

    # Price from $10-$30
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

    # Price from $30-$50
    def test_price_under_thirty_to_fifty1(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(45, 5, .1), 50.83)

    def test_price_under_thirty_to_fifty2(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(45, 5, .15), 48.71)

    def test_price_under_thirty_to_fifty3(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(45, 5, .2), 46.59)

    def test_price_under_thirty_to_fifty4(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(45, 10, .1), 46.06)

    def test_price_under_thirty_to_fifty5(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(45, 10, .15), 44.20)

    def test_price_under_thirty_to_fifty6(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(45, 10, .2), 42.35)

    # Price over $50
    def test_price_under_over_fifty1(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(70, 5, .1), 62.01)

    def test_price_under_over_fifty2(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(70, 5, .15), 58.56)

    def test_price_under_over_fifty3(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(70, 5, .2), 55.12)

    def test_price_under_over_fifty4(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(70, 10, .1), 57.24)

    def test_price_under_over_fifty5(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(70, 10, .15), 54.06)

    def test_price_under_over_fifty6(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(70, 10, .2), 50.88)


if __name__ == '__main__':
    unittest.main()
