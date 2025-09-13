text = input().strip()
index_count = 0

for e in text:
    index_count += 1
    for j in range(index_count):
        print(e * (j + 1))