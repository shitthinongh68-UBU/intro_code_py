""" count  = dict()

n = int(input())
total = int()

for i in range(n):
    customers, product, price, amount = input().split(',')
    data = list([product, int(price), int(amount)])
    count[customers] = count.get(customers, list()) + data
    print(count)

max_row = list(max(count.items(), key=lambda x: x[1][2]))

print(max_row[1][0])
print(max_row[1][2])
print(max_row[1][2] * max_row[1][1]) """

from collections import defaultdict

product_data = defaultdict(lambda: [0, 0])

n = int(input())

for _ in range(n):
    customer, product, price, amount = input().split(',')
    customer = customer.strip()
    product = product.strip()
    price = int(price.strip())
    amount = int(amount.strip())

    product_data[product][0] += amount
    product_data[product][1] += price * amount

max_product = max(product_data.items(), key=lambda x: x[1][1])

print(max_product[0])
print(max_product[1][0])
print(max_product[1][1])


