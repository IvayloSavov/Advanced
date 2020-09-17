from collections import deque

cups_capacity = deque(map(int, input().split())) # filling from the first entered cup -> queue

bottles_with_water_l = list(map(int, input().split())) # taking from the last -> stack

wasted_liters = 0
while cups_capacity and bottles_with_water_l:
    bottle = bottles_with_water_l.pop()
    cups_capacity[0] -= bottle

    if cups_capacity[0] <= 0:
        wasted_liters -= cups_capacity.popleft()

if not cups_capacity:
    print("Bottles: ", end="")
    while bottles_with_water_l:
        print(bottles_with_water_l.pop(), end=" ")
else:
    print("Cups: ", end="")
    while cups_capacity:
        print(cups_capacity.popleft(), end=" ")

print(f"\nWasted litters of water: {wasted_liters}")