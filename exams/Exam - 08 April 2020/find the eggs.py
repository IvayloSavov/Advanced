def find_strongest_eggs(sequence, count_sub_list):
    sub_lists = [[] for _ in range(count_sub_list)]
    index = 0

    for ch in sequence:
        sub_lists[index].append(ch)
        index += 1
        if index == len(sub_lists):
            index = 0

    strongest_eggs = []
    for eggs in sub_lists:
        middle_index = len(eggs) // 2
        if eggs[middle_index] > eggs[middle_index - 1] and eggs[middle_index] > eggs[middle_index + 1]:
            if sum(eggs[middle_index + 1:]) > sum(eggs[:middle_index]):
                strongest_eggs.append(eggs[middle_index])

    return strongest_eggs


test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))

