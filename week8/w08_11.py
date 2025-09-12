email_list = list()
number_of_data = int(input())

for i in range(number_of_data):
    fname, lname, enroll_year = input().lower().strip().split(',')
    email_for_check = fname + '.' + lname[:2] + '.' + enroll_year[-2:]

    if email_for_check in email_list:
        email_list.append(fname + '.' + lname[:3] + '.' + enroll_year[-2:])
    else:
        email_list.append(email_for_check)
    
print(*email_list, sep='@ubu.ac.th\n', end='@ubu.ac.th')