score_store = list()

for i in range (5):
    score_input = int(input('Enter data: '))
    score_store.append(score_input)
    
score_store.sort()
# 1 2 3 4
score_store.reverse()
# 4 3 2 1

for i in range (3):
    print(f'{score_store[i]}', end = " ")
    # 7 3 2
    
# print(f'{score_store[0]} {score_store[1]} {score_store[2]}')