from collections import deque

quantity_food = int(input())
orders = deque(map(int, input().split(" ")))
canceled_orders = deque()
print(max(orders))

while len(orders) > 0:
    order_current_client = orders.popleft()
    if order_current_client <= quantity_food:
        quantity_food -= order_current_client
    else:
        orders.appendleft(order_current_client)
        break

if len(orders) > 0:
    orders = list(map(str, orders))
    print(f"Orders left: {' '.join(orders)}")
else:
    print("Orders complete")