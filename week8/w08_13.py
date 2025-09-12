price, amount, weight = input().split(',')
discount = int(input())

price = float(price)
amount = float(amount)
weight = float(weight)

total = price*amount

if discount > 0:
    total = total - total * discount/100
if total >= 1000:
    delivery = 0
else:
    delivery = 40*weight
    total = total + delivery

print(f'Total: {total:.1f} baht ')