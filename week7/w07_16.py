student_data = dict()

number_of_data = int(input())

for i in range (number_of_data):
    stu_name, stu_score = input().strip().split()
    stu_score = float(stu_score)
    if stu_name not in student_data:
        student_data[stu_name] = stu_score
    else:
        stu_score[stu_name] += stu_score
        
student_data_keys = student_data.keys()
student_data_keys = sorted(student_data_keys)

for i in student_data_keys:
    print(f'{i} {student_data[i]:.1f}')