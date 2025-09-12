player_score = {
    'playerA': 0,
    'playerB': 0,
    'playerC': 0,
    'playerD': 0
}

n = int(input())

for i in range(n):
    data = input().split()
    for item in data:
        name, score = item.split(':')
        player_score[name] += int(score)

print(f'playerA:{player_score["playerA"]}')
print(f'playerB:{player_score["playerB"]}')
print(f'playerC:{player_score["playerC"]}')
print(f'playerD:{player_score["playerD"]}')