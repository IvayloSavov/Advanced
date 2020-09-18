def create_set_with_numbers(count_elements):
    return set(input() for _ in range(count_elements))


def intersection(set_1: set, set_2: set):
    return print("\n".join(set(map(str, set_1.intersection(set_2)))))


n, m = tuple(map(int, input().split(" ")))
intersection(create_set_with_numbers(n), create_set_with_numbers(m))