text = input().strip()

upper_count = lower_count = numberic_count = 0

'''AlphaBET 999'''

for i in text:
    if i.isupper(): 
        upper_count += 1 #ABET 4
    elif i.islower(): 
        lower_count += 1 #lpha 4
    elif i.isnumeric(): 
        numberic_count += 1 #999 3
    
print(upper_count)
print(lower_count)
print(numberic_count)