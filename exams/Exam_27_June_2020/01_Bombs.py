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

        count_bombs = 0
        for bomb, value in type_bombs.items():
            if value[1] >= 3:
                count_bombs += 1
                continue
            else:
                break

        if count_bombs >= 3:
            success = True
            break

    return success, type_bombs


bomb_effects = deque(map(int, input().split(", ")))
bomb_casings = deque(map(int, input().split(", ")))
res = bombs(bomb_effects, bomb_casings)

if res[0]:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
else:
    print(f"Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")
else:
    print("Bomb Casings: empty")

for type_bomb, values in sorted(res[1].items()):
    print(f"{type_bomb}: {values[1]}")
