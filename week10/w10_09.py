count = int(input())
text_list = list()

for i in range(count):
    text_list.append(input().strip())
    text_for_process = text_list[i].replace(' ','').lower()
    text_lenght = len(text_for_process)
    vowels_count = 0
    for e in text_for_process:
        if e in 'aeiou':
            vowels_count += 1
    print(text_list[i], text_lenght - vowels_count, vowels_count)