bd_year = int(input('Enter your birth year:'))
age = 2568 - bd_year

if age >= 18:
    print(f'You are {age} years old.')
    print('Welcome to our website.')
else:
    print(f'You are {age} years old.')
    print('You cannot access this content!')