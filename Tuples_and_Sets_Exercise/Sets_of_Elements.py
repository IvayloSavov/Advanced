def create_set_with_numbers(count_elements):
    numbers = set()
    for _ in range(count_elements):
        number = input()
        numbers.add(number)

    return numbers


def intersection(set_1: set, set_2: set):
    unique_elements = set_1.intersection(set_2)
    return set(map(str, unique_elements))


n, m = tuple(map(int, input().split(" ")))
set_n = create_set_with_numbers(n)
set_m = create_set_with_numbers(n)
unique_elements = intersection(set_n, set_m)
print("\n".join(unique_elements))
