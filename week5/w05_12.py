name_arry = list()

for i in range (10):
    add_name = input().strip()
    name_arry.append(add_name)
    
find_name = input('Find student: ')
print(name_arry.index(find_name) + 1)
















""" name_arry = list()
for i in range (0,10):
    add_name = input().strip()
    name_arry.append(add_name)

print('Find student: ', end='')
find_name = input().strip()
print(name_arry.index(find_name) + 1) """