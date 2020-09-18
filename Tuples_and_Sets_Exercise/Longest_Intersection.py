def longest_intersection_def(count_inputs):

    longest_intersection_set = set()

    for _ in range(count_inputs):
        first_range, second_range = tuple(input().split("-"))

        first_start, first_end = tuple(first_range.split(",")) # tuple(map(int, first_range.split(",")))
        second_start, second_end = tuple(second_range.split(","))

        # first_sequence_of_numbers = {digit for digit in range(int(first_start), int(first_end) + 1)}
        # second_sequence_of_numbers = {digit_2 for digit_2 in range(int(second_start), int(second_end) + 1)}

        first_sequence_of_numbers = set(range(int(first_start), int(first_end)))
        second_sequence_of_numbers = set(range(int(second_start), int(second_end)))

        current_intersection = first_sequence_of_numbers.intersection(second_sequence_of_numbers)

        if len(current_intersection) > len(longest_intersection_set):
            longest_intersection_set = current_intersection

    return longest_intersection_set


def printing_results(set_intersection):
    print(f"Longest intersection is [{', '.join(list(map(str, sorted(set_intersection))))}] with length {len(set_intersection)}")


n = int(input())
longest_intersection = longest_intersection_def(n)
printing_results(longest_intersection)
