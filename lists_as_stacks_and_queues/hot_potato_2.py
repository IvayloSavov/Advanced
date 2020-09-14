from collections import deque

people = deque(input().split(" "))
n_toss = int(input())

while len(people) > 1:
    for _ in range(n_toss):
        people.append(people.popleft())
    loser = people.pop()
    print(f"Removed {loser}")

winner = people.pop()
print(f"Last is {winner}")