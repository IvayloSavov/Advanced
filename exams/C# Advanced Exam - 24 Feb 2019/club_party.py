from collections import deque

max_capacity = int(input())
line = input().split()
halls = {}
peoples = deque([])

index = 0
while line:
    element = line.pop()
    if element.isalpha():
        halls[element] = []
    elif halls:                             # not hall, so we have to check if we have a hall to add the people
        current_hall = list(halls.keys())[0]
        if sum(halls[current_hall]) + int(element) <= max_capacity:
            halls[current_hall].append(int(element))
        else:
            if len(halls) > 1:  # not enough space in the previous hall, so we check if we have another one otherwise
                # the current amount of people is skipped
                next_hall = list(halls.keys())[1]
                halls[next_hall].append(int(element))
            print(f"{current_hall} -> {', '.join(map(str, halls[current_hall]))}")
            halls.pop(current_hall)