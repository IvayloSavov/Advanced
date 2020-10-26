from collections import deque


def bombs(effects: deque, casings: deque):
    type_bombs = {
        "Datura Bombs": [40, 0],
        "Cherry Bombs": [60, 0],
        "Smoke Decoy Bombs": [120, 0],
    }

    success = False

    while effects and casings:
        current_casing = casings[-1]
        current_effect = effects[0]

        for bomb, value in type_bombs.items():
            is_found_bomb = False
            if current_casing + current_effect == value[0]:
                type_bombs[bomb][1] += 1
                casings.pop()
                effects.popleft()
                is_found_bomb = True
                break

        if not is_found_bomb:
            casings[-1] -= 5

        if all([value[1] >= 3 for value in type_bombs.values()]):
            success = True
            break

    return success, type_bombs


bomb_effects = deque(map(int, input().split(", ")))
bomb_casings = deque(map(int, input().split(", ")))
res, bombs_res = bombs(bomb_effects, bomb_casings)

print("Bene! You have successfully filled the bomb pouch!") if res else print("You don't have enough materials to "
                                                                              "fill the bomb pouch.")
print(f"Bomb Effects: {', '.join(map(str, bomb_effects)) if bomb_effects else 'empty'}")
print(f"Bomb Casings: {', '.join(map(str, bomb_casings)) if bomb_casings else 'empty'}")

for type_bomb, values in sorted(bombs_res.items()):
    print(f"{type_bomb}: {values[1]}")