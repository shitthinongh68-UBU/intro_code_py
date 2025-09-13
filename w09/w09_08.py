text = str()
list_of_text = list()

while True:
    text = input().strip()
    if text != 'done':
        list_of_text.append(text)
    else:
        break

for i in list_of_text:
    if i.lstrip('-').isnumeric():
        if int(i) < 0:
            print(f'{i} is negative')
        elif int(i) == 0:
            print('0 is zero')
        else:
            print(f'{i} is positive')
    else:
        print('invalid input')        