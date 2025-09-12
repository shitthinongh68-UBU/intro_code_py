text = input('Enter text>>').strip()
text_len = len(text)

if text_len % 2 == 0:
    text = text[::-1]

for i in range(text_len): print(text, end='\n')