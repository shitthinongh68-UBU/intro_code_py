count = int(input())
text_list = list()


for i in range(count):
    text_lenght = vowels_count = 0
    text_list.append(input().strip())
    text_for_process = text_list[i].replace(' ','').lower()
    for e in text_for_process:
        if e.isalpha():
            text_lenght += 1
        if e in 'aeiou':
            vowels_count += 1
    
    print(text_list[i], text_lenght - vowels_count, vowels_count)