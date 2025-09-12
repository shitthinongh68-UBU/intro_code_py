text = input().strip().lower()
count = 0

while count < len(text):
    if text[count] in {'a','e','i','o','u'}:
        print('vowel')
    elif text[count] not in {'a','e','i','o','u'}:
        print('consonant')
    count += 1