from collections import deque

materials = deque(map(int, input().split()))
magic_levels = deque(map(int, input().split()))

presents = {"Doll": {"magic needed": 150, "count": 0}, "Wooden train": {"magic needed": 250, "count": 0},
            "Teddy bear": {"magic needed": 300, "count": 0}, "Bicycle": {"magic needed": 400, "count": 0}}

while materials and magic_levels:
    current_material = materials.pop()
    current_magic_lvl = magic_levels.popleft()

    if current_material == 0 and current_magic_lvl == 0:
        continue
    elif current_material == 0 and current_magic_lvl != 0:
        magic_levels.appendleft(current_magic_lvl)
        continue
    elif current_material != 0 and current_magic_lvl == 0:
        materials.append(current_material)
        continue

    current_present = current_material * current_magic_lvl

    if current_present < 0:
        current_present = current_material + current_magic_lvl
        materials.append(current_present)
        continue

    found_present = False
    for present in presents.keys():
        if presents[present]["magic needed"] == current_present:
            found_present = True
            presents[present]["count"] += 1
            break

    if not found_present:
        current_material += 15
        materials.append(current_material)

if (presents["Doll"]["count"] and presents["Wooden train"]["count"]) or (presents["Teddy bear"]["count"] and
                                                                         presents["Bicycle"]["count"]):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, list(materials)[::-1]))}")

if magic_levels:
    print(f"Magic left: {', '.join(map(str, list(magic_levels)))}")

for present, values in sorted(presents.items()):
    if values["count"] >= 1:
        print(f"{present}: {values['count']}")