number = int(input())


for i in range(2,number + 1):
    prime_index = 0
    for j in range(i+1):
        temp_j = j + 1
        if i % (temp_j) == 0:
            prime_index += 1
            
    if prime_index <= 2: print(i)