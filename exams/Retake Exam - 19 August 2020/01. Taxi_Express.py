from collections import deque

customers = deque(map(int, input().split(", ")))
taxis = deque(map(int, input().split(", ")))
total_time = 0

while taxis and customers:
    current_customer = customers[0]
    current_taxi = taxis[-1]

    if current_taxi >= current_customer:
        total_time += current_customer
        customers.popleft()
    taxis.pop()

if customers:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(map(str, customers))}")
else:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")