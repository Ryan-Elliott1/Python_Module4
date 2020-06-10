def calculate_price(price, cash_coupon, percent_coupon):
    total = 0
    tax_rate = 0.06
    if price < 10:
        total = price - cash_coupon
        total = (total - (total * percent_coupon)) + 5.95
        total = (total + (total * tax_rate))
        total = round(total, 2)
        return total


if __name__ == '__main__':
    print(calculate_price(9, 10, .2))

