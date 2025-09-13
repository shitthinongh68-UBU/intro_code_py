number = float()
list_of_number = list()

while True:
    number = float(input())
    if number != -1:
        list_of_number.append(number)
    else:
        break
    


print(f'{sum(list_of_number) / len(list_of_number):.1f}')