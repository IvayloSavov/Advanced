def find_strongest_eggs(*args):
    string = args[0]
    counts_subs = args[1]

    sub_lists = []
    strongest_elements = []
    for i in range(counts_subs):
        sub_lists.append([string[j] for j in range(i, len(string), counts_subs)])
        middle_index = len(sub_lists[i]) // 2
        if sub_lists[i][middle_index] > sub_lists[i][middle_index + 1] > sub_lists[i][middle_index - 1] and \
                sub_lists[i][middle_index] > sub_lists[i][middle_index - 1]:
            strongest_elements.append(sub_lists[i][middle_index])

    return strongest_elements
