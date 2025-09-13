num_list = input().split()
pair_sum10 = False

for i in num_list:
    for j in range(len(num_list)):
        if i == num_list[j]:
            continue
        elif int(i) + int(num_list[j]) == 10:
            pair_sum10 = True


if pair_sum10 != True: print('false')
else: print('true')