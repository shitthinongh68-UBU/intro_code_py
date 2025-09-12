input_count = int(input())
input_arry = set()

for i in range (input_count):
    input_arry.add(input().strip())
    
different_arry = sorted(input_arry)

print(','.join(different_arry))