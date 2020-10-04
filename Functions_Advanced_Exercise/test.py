from collections import deque

a = deque([1, 2, 3, 4, 5])


a = deque(a.popleft() for _ in range(2))
print(a)