morse_code_list = ['-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
number = input().strip()

if number.isnumeric():
    for e in number:
        print(morse_code_list[int(e)], end=' ')
else:
    print('error')