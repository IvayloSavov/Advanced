from collections import deque
from itertools import co

def get_repeating_DNA(*args):
    for string_1 in args:
        letters = ["A", "G", "C", "T"]
        for letter in string_1:
            if letter not in letters:
                continue
        string = deque(string_1)
        repeating_sequence = []
        string_to_check = "".join(string)

        is_break = False
        while len(string) >= 10:
            current_sequence = ""

            for i in range(10):
                if not string:
                    is_break = True
                    break
                ch = string.popleft()
                # if ch in letters:
                #     current_sequence += ch
                current_sequence += ch

            if len(string) == 1:
                ch = string.popleft()
                scnd_str = current_sequence[1:] + ch
                if current_sequence == scnd_str:
                    if current_sequence not in repeating_sequence:
                        repeating_sequence.append(current_sequence)

            elif len(current_sequence) == 10 and string_to_check.count(current_sequence) > 1:
                if current_sequence not in repeating_sequence:
                    repeating_sequence.append(current_sequence)

            if is_break:
                break

    return repeating_sequence


test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)
test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"
result = get_repeating_DNA(test)
print(result)
test = "AAAAAAAAAAA"
result = get_repeating_DNA(test)
print(result)
