stu_data = dict()
number_of_data = int(input())

for i in range (number_of_data):
    stu_name, stu_score = input().strip().split()
    stu_score = float(stu_score)
    stu_data[stu_name] = stu_score

sorted_stu_data = list(sorted(stu_data.items(), key=lambda x: x[1], reverse=True))

for j in range (len(sorted_stu_data)):
    print(f'{sorted_stu_data[j][0]} {sorted_stu_data[j][1]:.1f}')