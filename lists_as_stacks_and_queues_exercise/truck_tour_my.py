from collections import deque
n = int(input())
tank = 0
pumps = deque()

for _ in range(n):
    tokens = list(map(int, input().split()))
    pumps.append(tokens)

for i in range(n):
    print(pumps)
    fuel = 0
    is_valid = True
    for _ in range(n):
        current_pump = pumps.popleft()
        amount_of_fuel, distance = current_pump
        fuel += amount_of_fuel - distance
        if fuel < 0:
            is_valid = False
        pumps.append(current_pump)

    if is_valid:
        print(i)
        break

    pumps.rotate(-1)