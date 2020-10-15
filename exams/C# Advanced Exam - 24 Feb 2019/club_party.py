from collections import deque

max_capacity = int(input())
line = input().split()
halls = {}
peoples = deque([])

while line:
    element = line.pop()
    if element.isalpha():
        halls[element] = []
    else:
        if halls:
            peoples.append(int(element))

left_people_from_previous_hall = 0
for hall, people_in_hall in halls.items():
    cur_people_in_hall = people_in_hall
    if left_people_from_previous_hall:
        cur_people_in_hall.append(left_people_from_previous_hall)
        left_people_from_previous_hall = 0
    while peoples:
        cur_people = peoples.popleft()
        if sum(cur_people_in_hall) + cur_people < max_capacity:
            cur_people_in_hall.append(cur_people)
        else:
            print(f"{hall} -> {', '.join(map(str, cur_people_in_hall))}")
            left_people_from_previous_hall = cur_people
            break

    if not peoples:
        break
