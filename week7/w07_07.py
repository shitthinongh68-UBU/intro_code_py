""" product_price = float(input('Enter product price (THB): '))
percent_discount = int(input("%discount: "))

Sale_price = product_price - (product_price * (percent_discount / 100))

print(f'{Sale_price:.1f}') """

product_price = float(input())
percent_discount = int(input())

Sale_price = product_price - (product_price * (percent_discount / 100))

print(f'Enter product price (THB): %discount: Sale price (THB): {Sale_price:.1f}')

