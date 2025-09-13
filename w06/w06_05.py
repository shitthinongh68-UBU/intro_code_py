user1_follower = input().strip().split()
user2_follower = input().strip().split()

user1_follower = set(user1_follower)
user2_follower = set(user2_follower)

common_follower = user1_follower.intersection(user2_follower)
common_follower = sorted(list(common_follower))

print(len(common_follower))
print(*common_follower)