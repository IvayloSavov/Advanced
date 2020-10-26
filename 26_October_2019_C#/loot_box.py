from collections import deque

first_box = deque(map(int, input().split()))
second_box = list(map(int, input().split()))

claimed_items = []

while True:
    res = first_box[0] + second_box[-1]
    if res % 2 == 0:
        claimed_items.append(res)
        first_box.popleft()
        second_box.pop()
    else:
        first_box.append(second_box.pop())

    if not first_box:
        print("First lootbox is empty")
        break
    elif not second_box:
        print("Second lootbox is empty")
        break

if sum(claimed_items) >= 100:
    print(f"Your loot was epic! Value: {(sum(claimed_items))}")
else:
    print(f"Your loot was poor... Value: {(sum(claimed_items))}")

