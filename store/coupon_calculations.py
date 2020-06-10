def calculate_price(price, cash_coupon, percent_coupon):
    total = 0
    tax_rate = 0.06
    if price < 10:
        total = price - cash_coupon
        total = (total - (total * percent_coupon))
        total = (total + (total * tax_rate)) + 5.95
        total = round(total, 2)
        return total


if __name__ == '__main__':
    print(calculate_price(9, 10, 0.2))

