def periodic_table(count_lines):
    elements = set()

    for _ in range(count_lines):
        elements_input = set(input().split(" "))
        elements.union(elements_input)

    return "\n".join(sorted(elements))


print(periodic_table(int(input())))