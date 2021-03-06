def periodic_table(count_lines):
    elements = set()

    for _ in range(count_lines):
        elements_input = tuple(input().split(" "))
        for element in elements_input:
            elements.add(element)

    return "\n".join(sorted(elements))


print(periodic_table(int(input())))