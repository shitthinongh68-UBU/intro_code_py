price = float(input())
b_price = price * 100 / 107
print(f'product price: {b_price:,.2f} baht')
vat = price - b_price
print(f'vat: {vat:,.2f} baht')
