price = float(input())
b_price = price * 100 / 107
vat = price - b_price
print(f'product price: {b_price:.2f} baht')
print(f'vat: {vat:.2f} baht')