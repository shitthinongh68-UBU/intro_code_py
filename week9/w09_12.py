computer = int(input('enter number of computers>>>'))
inuse_computer = list()
while True:
    user_input = input('enter code>>>').strip().split()
    if len(user_input) == 1:
        command = user_input[0]
    elif len(user_input) == 2:
        command, stu_id = user_input[0], user_input[1]
    
    if command == 'in':
        if len(inuse_computer) == computer:
            print('FULL')
        else:
            inuse_computer.append(stu_id)
            print('OK')
    elif command == 'out':
        inuse_computer.remove(stu_id)
        print(f'{stu_id} has left')
    elif command == 'status':
        print(*inuse_computer, sep=',')
    elif command == 'quit':
        print('finish')
        break