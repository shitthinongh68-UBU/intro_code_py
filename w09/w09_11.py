number = '0123456789'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = lowercase.upper()
special_characters = '`~!@#$%^&-_=+[{]}.'
while True:
    password = input().strip()
    password_check = {
        'lenght' : False,
        'number' : False,
        'lowercase' : False,
        'uppercase' : False,
        'spacialchar' : False
                      }  
    if len(password) >= 12: password_check['lenght'] = True
    for char in password:
        if char in '0123456789': password_check['number'] = True
        if char in 'abcdefghijklmnopqrstuvwxyz': password_check['lowercase'] = True
        if char in 'ABCDEFGHIJKLMNOPQRSTUVWXY' : password_check['uppercase'] = True
        if char in '`~!@#$%^&-_=+[{]}.' : password_check['spacialchar'] = True
    
    if False not in list(password_check.values()):
        print('valid')
    else:
        print('invalid')