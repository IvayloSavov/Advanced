from collections import deque


def find_strongest_eggs(*args):
    eggs = deque(args[0])
    count_sub_lists = args[1]
    sub_lists = [[] for _ in range(count_sub_lists)]
    index = 0
    while eggs:
        current_egg = eggs.popleft()
        sub_lists[index].append(current_egg)
        index += 1
        if index == len(sub_lists):
            index = 0

    strongest_eggs = []

    for s_list in sub_lists:
        middle_egg_index = len(s_list) // 2
        middle_egg = s_list[middle_egg_index]

        if middle_egg > s_list[middle_egg_index + 1] and middle_egg > s_list[middle_egg_index - 1]:
            if sum(s_list[middle_egg_index + 1:]) > sum(s_list[:middle_egg_index]):
                strongest_eggs.append(middle_egg)

    return strongest_eggs


test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))

