from collections import deque

all_cups = deque(map(int, input().split(" ")))
all_bottles = deque(map(int, input().split(" ")))
not_enough_bottles = False

wasted_liters_of_water = 0


while all_bottles and all_cups:
    current_cup = all_cups.popleft()
    current_bottle = 0

    while current_cup > 0:
        if current_bottle <= 0 and all_bottles:
            current_bottle = all_bottles.pop()
        else:
            not_enough_bottles = True
            break

        if current_cup > current_bottle:
            current_cup -= current_bottle
            current_bottle -= current_bottle

        elif current_bottle >= current_cup:
            current_bottle -= current_cup
            current_cup -= current_cup
            wasted_liters_of_water += current_bottle

    if not_enough_bottles:
        break

if not all_cups:
    all_bottles.reverse()
    all_bottles = ' '.join(map(str, all_bottles))
    print(f"Bottles: {all_bottles}")
else:
    all_cups = " ".join(map(str, all_cups))
    print(f"Cups: {all_cups}")

print(f"Wasted litters of water: {wasted_liters_of_water}")