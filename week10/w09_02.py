count = int(input())
number = list()

for i in range(count):
    number.append(int(input()))

print("sum =",sum(number))
print("range =", max(number) - min(number))