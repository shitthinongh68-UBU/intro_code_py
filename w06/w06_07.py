email_name = input().lower().strip()
email_lastname = input().lower().strip()
email_bdyear = str(input())

print(f'{email_name}.{email_lastname[:2]}.{email_bdyear[2:]}@ubu.ac.th')