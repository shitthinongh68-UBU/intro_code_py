number = int(input())

for i in range(1,number+1):
    sum_digit = 0
    for j in str(i):
        sum_digit += int(j)
    if '7' in str(i):
        print('7-up')
    elif sum_digit == 7:
        print('7-up')
    elif i % 7 == 0:
        print('7-up')
    else:
        print(i)
