from collections import deque

all_customers = deque(map(int, input().split(", ")))
all_taxis = deque(int(t) for t in input().split(", "))

total_time = 0

while all_customers and all_taxis:
    customer = all_customers.popleft()
    taxi = all_taxis.pop()

    if taxi >= customer:
        total_time += customer
    else:
        all_customers.appendleft(customer)

if not all_customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")

elif not all_taxis and all_customers:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(c) for c in all_customers])}")