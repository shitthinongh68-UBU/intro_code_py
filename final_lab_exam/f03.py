count = int(input())
text = input().strip()

for i in range(count):
    print(text[0] * (i + 1) + text[1] * ((count - 1) - i))