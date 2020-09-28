from collections import deque

presents = {
    "Doll": {"magic needed": 150, "count": 0},
    "Wooden train": {"magic needed": 250, "count": 0},
    "Teddy bear": {"magic needed": 300, "count": 0},
    "Bicycle": {"magic needed": 400, "count": 0},
}

materials = deque(map(int, input().split()))
magic_levels = deque(map(int, input().split()))

while materials and magic_levels:
    current_material = materials.pop()
    current_magic = magic_levels.popleft()

    if current_material == 0 and current_magic > 0:
        magic_levels.appendleft(current_magic)
        continue

    if current_magic == 0 and current_material > 0:
        materials.append(current_material)
        continue

    if current_material == 0 and current_magic == 0:
        continue

    total_magic = current_magic * current_material
    if total_magic < 0:
        new_material = current_magic + current_material
        materials.append(new_material)
        continue

    found_present = False

    for present, info in presents.items():
        if info["magic needed"] == total_magic:
            found_present = True
            presents[present]["count"] += 1

    if not found_present:
        current_material += 15
        materials.append(current_material)

is_done = False

if (presents["Doll"]["count"] >= 1 and presents["Wooden train"]["count"] >= 1) \
        or (presents["Teddy bear"]["count"] >= 1 and presents["Bicycle"]["count"] >= 1):
    is_done = True

if is_done:
    print("The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if materials:
    materials.reverse()
    print(f"Materials left: {', '.join(list(map(str, materials)))}")

if magic_levels:
    print(f"Magic left: {', '.join(list(map(str, magic_levels)))}")

filtered_presents = [p for p in sorted(presents) if presents[p]["count"] >= 1]

for present in filtered_presents:
    print(f"{present}: {presents[present]['count']}")