stu_data = dict()
while True:
    text = input()
    if text == "-1":
        break
    else:
        stu_id, score1, score2 = text.strip().split()
        score1 = float(score1)
        score2 = float(score2)
        stu_data[stu_id] = (score1 + score2) / 2

stu_data_keys = list(stu_data.keys())
count = 0

while count < len(stu_data_keys):
    print(stu_data_keys[count], '{:.1f}'.format(stu_data[stu_data_keys[count]]))
    count += 1