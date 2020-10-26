from collections import deque

males = list(map(int, input().split()))
females = deque(map(int, input().split()))
matches = 0

while males and females:
    if males[-1] <= 0:
        males.pop()
        continue

    if females[0] <= 0:
        females.popleft()
        continue

    if males[-1] % 25 == 0:
        males.pop()
        if males:
            males.pop()
        continue

    if females[0] % 25 == 0:
        females.popleft()
        if females:
            females.popleft()
        continue

    if males and females:
        if males[-1] == females[0]:
            matches += 1
            males.pop()
            females.popleft()
        else:
            males[-1] -= 2
            females.popleft()

print(f"Matches: {matches}")
print(f"Males left: {'none' if not males else ', '.join((map(str, males[::-1])))}")
print(f"Females left: {'none' if not females else ', '.join((map(str, females)))}")