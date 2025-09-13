A = B = str()
A_score = B_score = 0
 
while A_score < 3 and B_score < 3:
    A, B = input().strip().split()
    if A ==  B:
        continue
    elif (A == 'rock' and B == 'scissors') or (A == 'scissors' and B == 'paper') or (A == 'paper' and B == 'rock'):
        A_score += 1
    else:
        B_score += 1

if A_score > B_score:
    print(f'A wins the game ({A_score}-{B_score}).')
else:
    print(f'B wins the game ({B_score}-{A_score}).')