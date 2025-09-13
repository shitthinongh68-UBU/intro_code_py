studentID, studentSCORE = input().split(',')
studentSCORE = float(studentSCORE)

if studentSCORE >= 60:
    print(f'{studentID} pass')
else:
    print(f'{studentID} fail')