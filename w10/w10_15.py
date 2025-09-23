row1 = {
    0: '*****',
    1: '    *',
    2: '*****',
    3: '*****',
    4: '*   *',
    5: '*****',
    6: '*****',
    7: '*****',
    8: '*****',
    9: '*****'
}
row2 = {
    0: '*   *',
    1: '    *',
    2: '    *',
    3: '    *',
    4: '*   *',
    5: '*    ',
    6: '*    ',
    7: '    *',
    8: '*   *',
    9: '*   *'
}
row3 = {
    0: '*   *',
    1: '    *',
    2: '*****',
    3: '*****',
    4: '*****',
    5: '*****',
    6: '*****',
    7: '    *',
    8: '*****',
    9: '*****'
}
row4 = {
    0: '*   *',
    1: '    *',
    2: '*    ',
    3: '    *',
    4: '    *',
    5: '    *',
    6: '*   *',
    7: '    *',
    8: '*   *',
    9: '    *'
}
row5 = {
    0: '*****',
    1: '    *',
    2: '*****',
    3: '*****',
    4: '    *',
    5: '*****',
    6: '*****',
    7: '    *',
    8: '*****',
    9: '*****'
}

number_input = input().strip()


row1_sign = []
row2_sign = []
row3_sign = []
row4_sign = []
row5_sign = []

if number_input.isnumeric():
    for i in number_input:
        d = int(i)

        row1_sign.append(row1[d])
        row2_sign.append(row2[d])
        row3_sign.append(row3[d])
        row4_sign.append(row4[d])
        row5_sign.append(row5[d])


    print(' '.join(row1_sign))
    print(' '.join(row2_sign))
    print(' '.join(row3_sign))
    print(' '.join(row4_sign))
    print(' '.join(row5_sign))
else:
    print('error')
