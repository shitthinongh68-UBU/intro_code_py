text = input().strip()
text_len = len(text)

if text_len == 10:
    print('perfect_10')
    
elif text_len > 10:
    print(text[:10])
    
elif text_len < 10:
    print(text + ('*' * (10 - text_len)))
else:
    print('CODE ERROR')