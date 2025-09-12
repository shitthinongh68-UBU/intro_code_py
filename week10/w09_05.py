def devision3 (num):
    if num % 3 == 0:
        return True
    else:
        return False

count = int(input())
perfect3 = list()

for i in range(count):
    number = int(input())
    if devision3(number):
        perfect3.append(number) 

print(*perfect3, sep=' ')