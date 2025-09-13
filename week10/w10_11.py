text = input().strip().lower()

if text[::-1] == text: print('yes')
else: print('no')