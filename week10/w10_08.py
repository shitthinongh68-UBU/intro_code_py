count = int(input())

current = 1
row = 1

while current <= count:
    for i in range(row):
        if current > count:
            break
        # Print space only if not last in row or last number
        if i == row - 1 or current == count:
            print(current, end='')
        else:
            print(current, end=' ')
        current += 1
    print()
    row += 1