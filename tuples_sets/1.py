import collections

number_occurence = collections.defaultdict(int)
numbers = map(float, input().split(" "))

for number in numbers:
    number_occurence[number] += 1

for number, occurence_count in number_occurence.items():
    print(f"{number} - {occurence_count} times")