from collections import deque # Грешно решение на truck_tour_my
n = int(input())
tank = 0
pumps = deque()

for _ in range(n):
    tokens = list(map(int, input().split()))
    pumps.append(tokens)

for i in range(n):
    print(pumps)
    tank = 0
    is_valid = True
    for _ in range(n):
        current_pump = pumps.popleft()
        amount_of_fuel, distance = current_pump
        tank += amount_of_fuel
        if tank - distance < 0:
            pumps.append(current_pump)
            is_valid = False
            break
        else:
            tank -= distance
            pumps.append(current_pump)

    if is_valid:
        print(i)
        break