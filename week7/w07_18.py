subscriber_set = set()

number_of_data = int(input())

for i in range (number_of_data):
    sub_pervideo = input().strip().split()
    for j in sub_pervideo:
        subscriber_set.add(j)

print(len(subscriber_set))