last_number = None

while True:
    number = int(input())
    if last_number == None:
        last_number = number
    elif number < last_number:
        print('end')
        break
    last_number = number
    print('yes')