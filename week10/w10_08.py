count = int(input())

row = 1
number_in_row = 0

for i in range(count):
    i += 1
    print(i, end=' ')
    number_in_row += 1
    
    if row == number_in_row:
        print()
        number_in_row = 0
        row += 1