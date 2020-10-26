from collections import deque
from operator import mul


def best_list_pureness(numbers, k):
    numbers = deque(numbers)
    biggest_pureness = sum([i * n for i, n in enumerate(numbers)])
    needed_rotation = 0
    for r in range(1, k + 1):
        numbers.appendleft(numbers.pop())
        current_pureness = 0
        for i, n in enumerate(numbers):
            current_pureness += mul(i, n)
        if current_pureness > biggest_pureness:
            biggest_pureness = current_pureness
            needed_rotation = r
    return f"Best pureness {biggest_pureness} after {needed_rotation} rotations"


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)


