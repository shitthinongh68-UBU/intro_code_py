
while True:
    user_input = input().strip()
    
    if user_input.isnumeric():
        
        number = int(user_input)
        count = 1
        prime_index = 0
        
        while count < number:
            
            division = number / count
            
            if division.is_integer():
                prime_index += 1
                
            count += 1
            
        if prime_index == 1 : 
            print('yes')
        else: 
            print('no')
            
    else:
        print('invalid input')