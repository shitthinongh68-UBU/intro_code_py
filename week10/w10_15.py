row1 = {
    0 : '*****',
    1 : '    *',
    2 : '*****',
    3 : '*****',
    4 : '*   *',
    5 : '*****',
    6 : '*****',
    7 : '*****',
    8 : '*****',
    9 : '*****'
}
row2 = {
    0 : '*   *',
    1 : '    *',
    2 : '    *',
    3 : '    *',
    4 : '*   *',
    5 : '*    ',
    6 : '*    ',
    7 : '    *',
    8 : '*   *',
    9 : '*   *'
}
row3 = {
    0 : '*   *',
    1 : '    *',
    2 : '*****',
    3 : '*****',
    4 : '*****',
    5 : '*****',
    6 : '*****',
    7 : '    *',
    8 : '*****',
    9 : '*****'
}
row4 = {
    0 : '*   *',
    1 : '    *',
    2 : '*    ',
    3 : '    *',
    4 : '    *',
    5 : '    *',
    6 : '*   *',
    7 : '    *',
    8 : '*   *',
    9 : '    *' 
}
row5 = {
    0 : '*****',
    1 : '    *',
    2 : '*****',
    3 : '*****',
    4 : '    *',
    5 : '*****',
    6 : '*****',
    7 : '    *',
    8 : '*****',
    9 : '*****'
}

number_input = input().strip()

if number_input.isnumeric():
    for i in number_input:
        print(row1[int(i)], end=' ')
        
    print()

    for i in number_input:
        print(row2[int(i)], end=' ')
        
    print()

    for i in number_input:
        print(row3[int(i)], end=' ')
        
    print()

    for i in number_input:
        print(row4[int(i)], end=' ')
        
    print()

    for i in number_input:
        print(row5[int(i)], end=' ')
    