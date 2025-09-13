email = str(input())

email_arry = email.split('.')
name = email_arry[0]
#shitthinon

print(f'{str(name[0].upper())}{str(name[1:])}')