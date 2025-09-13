stuID, stuSCORE = input().split(',')
stuSCORE = float(stuSCORE)

if 100 >= stuSCORE >= 80:
    print(stuID, 'A')
elif 80 > stuSCORE >= 75:
    print(stuID, 'B+')
elif 75 > stuSCORE >= 70:
    print(stuID, 'B')
elif 70 > stuSCORE >= 65:
    print(stuID, 'C+')
elif 65 > stuSCORE >= 60:
    print(stuID, 'C')
elif 60 > stuSCORE >= 55:
    print(stuID, 'D+')
elif 55 > stuSCORE >= 50:
    print(stuID, 'D')
elif stuSCORE < 50:
    print(stuID, 'F')
else:
    print('ERROR : DATA NOT IN RANGE')
