A = B = C = 1

A += B + 5
C = C + 3

while B <= 3:
    A = 0
    while A < B:
        C = B - C +1
        A = B - C
    B = B + 2
    A += 1
    print(A, B, C)