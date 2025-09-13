text = input().strip()
is_num = 0
is_lowstr = 0
is_upstr = 0

for e in text:
    if e.isnumeric(): is_num += 1
    if e.isupper(): is_upstr +=1
    if e.islower(): is_lowstr += 1
    
print(is_upstr, is_lowstr, is_num, sep='\n')