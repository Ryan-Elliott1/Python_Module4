"""
Program: coupon_calculations.py
Author: Ryan Elliott
Last date modified: 06/10/2020

This program calculates the price of a transaction
input price, cash coupon, and percent coupon
outputs total price with discounts, shipping and tax included
"""


def calculate_price(price, cash_coupon, percent_coupon):
    total = 0
    tax_rate = 0.06
    if price < 10:
        total = price - cash_coupon
        total = (total - (total * percent_coupon)) + 5.95
        total = (total + (total * tax_rate))
        total = round(total, 2)
        return total
    elif 10 <= price < 30:
        total = price - cash_coupon
        total = (total - (total * percent_coupon)) + 7.95
        total = (total + (total * tax_rate))
        total = round(total, 2)
        return total
    elif 30 <= price < 50:
        total = price - cash_coupon
        total = (total - (total * percent_coupon)) + 11.95
        total = (total + (total * tax_rate))
        total = round(total, 2)
        return total
    elif 50 <= price:
        total = price - cash_coupon
        total = (total - (total * percent_coupon))
        total = (total + (total * tax_rate))
        total = round(total, 2)
        return total


if __name__ == '__main__':
    print(calculate_price(70, 5, .15))

