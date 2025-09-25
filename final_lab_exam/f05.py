count = int(input())
major_name = list()
major_avgscore = list()

for i in range(count):
    raw_data = input().strip().split(',')
    score = list()
    for s in raw_data[1:]:
        score.append(float(s))
    avg_score = (sum(score) / len(score))
    major_name.append(raw_data[0].strip())
    major_avgscore.append(avg_score)

n = len(major_avgscore)
for i in range(n):
    for j in range(0, n-i-1):
        if major_avgscore[j] < major_avgscore[j+1]:
            major_avgscore[j], major_avgscore[j+1] = major_avgscore[j+1], major_avgscore[j]
            major_name[j], major_name[j+1] = major_name[j+1], major_name[j]

for i in range(len(major_name)):
    print(f'{major_name[i]} {major_avgscore[i]:.2f}')