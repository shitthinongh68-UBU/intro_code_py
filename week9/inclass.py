import random

ans = random(0,100)
guess = 0

while guess != ans:
    guess = int(input())
    if guess == ans:
        print('correct')
    elif guess > ans:
        print('มากไป')
    elif 