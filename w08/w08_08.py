stu_data = dict()
data_count = int(input())

for i in range(data_count):
    stuID, stuSCORE = input().split()
    stuSCORE = float(stuSCORE)
    stu_data[stuID] = stuSCORE

for i in stu_data:
    if  stu_data[i] > 100 or stu_data[i] < 0:
        print(i, 'error')
    elif stu_data[i] >= 60:
        print(i, 'pass')
    elif stu_data[i] < 60:
        print(i, 'fail')