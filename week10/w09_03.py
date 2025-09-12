count = int(input())

if count < 0:
    for i in range(abs(count),0,-1):
        print('Y'*i)
else:
    for i in range(count):
        print('Y'*(i+1))