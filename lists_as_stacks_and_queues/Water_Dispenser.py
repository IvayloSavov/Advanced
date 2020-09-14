from collections import deque

liters_in_dispenser = int(input())
people = deque()

while True:
    command = input()
    if command == "Start":
        break
    else:
        name = command
        people.append(name)

while True:
    command = input()
    if command.isdigit() and len(people) > 0:
        liters_to_drink = int(command)
        person = people.popleft()
        if liters_to_drink <= liters_in_dispenser:
            print(f"{person} got water")
            liters_in_dispenser -= liters_to_drink
        else:
            print(f"{person} must wait")

    elif command.startswith("refill "):
        liters_to_add = int(command.split(" ")[-1])
        liters_in_dispenser += liters_to_add

    elif command == "End":
        break

print(f"{liters_in_dispenser} liters left")

