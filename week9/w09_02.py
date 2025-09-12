line_count, line_char = input().strip().split()
line_count = int(line_count)
count = 0

while count < line_count:
    print(line_char * 8)
    count += 1