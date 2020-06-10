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


if __name__ == '__main__':
    print(calculate_price(9, 5, .1))

