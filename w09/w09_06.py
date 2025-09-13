number = str()
list_of_number = list()

while True:
    number = input().strip()
    if number.lstrip('-').isnumeric():
        number = int(number)
        list_of_number.append(number)
    elif number == 'done':
        break
    else:
        continue

for i in list_of_number:
    if i < 0:
        print(f'{i} is negative')
    elif i == 0:
        print('0 is zero')
    else:
        print(f'{i} is positive')