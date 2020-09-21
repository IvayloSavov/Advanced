from collections import deque

price_of_bullet = int(input())
gun_barrel_size = int(input())
bullets_in_one_barrel = deque(map(int, input().split()))
lockers = deque(map(int, input().split()))
value_of_intelligence = int(input())
is_fail = False

current_gun_barrel_size = gun_barrel_size

while lockers:
    if not current_gun_barrel_size:
        if not bullets_in_one_barrel:
            is_fail = True
            break
        else:
            print("Reloading!")
            current_gun_barrel_size = gun_barrel_size

    if bullets_in_one_barrel:
        bullet = bullets_in_one_barrel.pop()
    else:
        is_fail = True
        break

    current_gun_barrel_size -= 1
    value_of_intelligence -= price_of_bullet
    locker = lockers.popleft()

    if bullet <= locker:
        print("Bang!")
    else:
        print("Ping!")
        lockers.appendleft(locker)

if not is_fail:
    if not current_gun_barrel_size and bullets_in_one_barrel:
        print("Reloading!")
    print(f"{len(bullets_in_one_barrel)} bullets left. Earned ${value_of_intelligence}")
else:
    print(f"Couldn't get through. Locks left: {len(lockers)}")
