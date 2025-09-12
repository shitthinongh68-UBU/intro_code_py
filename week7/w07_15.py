a = list()

number_of_data = int(input('Number of data: '))
for i in range (number_of_data):
    data = int(input('Enter data: '))
    a.append(data)
    
total_of_a = sum(a)
mean_of_a = total_of_a / len(a)
max_of_a = max(a)
min_of_a = min(a)
range_of_a = max_of_a - min_of_a

print(f'Total: {total_of_a:.1f}')
print(f'Mean: {mean_of_a:.1f}')
print(f'Max: {max_of_a:.1f}')
print(f'Min: {min_of_a:.1f}')
print(f'Range: {range_of_a:.1f}')