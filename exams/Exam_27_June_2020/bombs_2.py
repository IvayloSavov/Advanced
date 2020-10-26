from collections import deque


bomb_effects = deque([int(i) for i in input().split(', ')])
bomb_casings = deque([int(i) for i in input().split(', ')])


BOMBS_MATERIALS = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs',
}


produced = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0,
}


def is_bomb_pouch_full(produced) -> bool:
    return all([value >= 3 for value in produced.values()])


while len(bomb_effects) > 0 and len(bomb_casings) > 0 and not is_bomb_pouch_full(produced):
    bomb_effect = bomb_effects.popleft()
    bomb_casing = bomb_casings.pop()
    bomb_sum = bomb_effect + bomb_casing

    managed_to_produce = False
    for cost, bomb_name in BOMBS_MATERIALS.items():
        if cost == bomb_sum:
            produced[bomb_name] += 1
            managed_to_produce = True
            break

    if not managed_to_produce:
        bomb_casing -= 5

        if bomb_casing >= 0:
            bomb_effects.appendleft(bomb_effect)
            bomb_casings.append(bomb_casing)


if not is_bomb_pouch_full(produced):
    print("You don't have enough materials to fill the bomb pouch.")
else:
    print('Bene! You have successfully filled the bomb pouch!')

print(f"Bomb Effects: {', '.join(map(str, bomb_effects)) if bomb_effects else 'empty'}")
print(f"Bomb Casings: {', '.join(map(str, bomb_casings)) if bomb_casings else 'empty'}")

for k, v in sorted(produced.items()):
    print(f'{k}: {v}')