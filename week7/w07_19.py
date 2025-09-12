count  = dict()

n = int(input())
total = int()

for i in range(n):
    customers, product, price, amount = input().split(',')
    total += int(price)*int(amount)
    count[product] = count.get(product, 0) + int(amount)

print(total)
max_item = max(count, key=count.get)
print(max_item)