from collections import deque

bullet_price = int(input())

gun_barrel_size = int(input())

bullets = list(map(int, input().split())) # stack

locks = deque(map(int, input().split())) # deque

intelligence_value = int(input())

reload_time = gun_barrel_size
bullets_cost = 0

while locks and bullets:
    if reload_time > 0:
        bullet = bullets.pop()
        bullets_cost += bullet_price
        reload_time -= 1

        if bullet <= locks[0]:
            print("Bang!")
            lock = locks.popleft()
        else:
            print("Ping!")
        # continue
    if reload_time == 0:
        if bullets:
            print("Reloading!")
            reload_time = gun_barrel_size
        # continue

if not locks:
    money_earned = intelligence_value - bullets_cost
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
elif not bullets:
    print(f"Couldn't get through. Locks left: {len(locks)}")