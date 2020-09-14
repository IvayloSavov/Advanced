from _collections import deque

people = deque()

while True:
    command = input()
    if command == "Paid":
        # people_who_paid = [people.pop() for _ in range(len(people))]
        # print(people.popleft())

        while len(people) > 0: # винаги така се пише, най-правилно е
            print(people.popleft())

    elif command == "End":
        break

    else:
        name = command
        people.append(name)

print(f"{len(people)} people remaining.")