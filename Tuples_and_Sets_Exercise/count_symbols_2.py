phrase = tuple(input())

unique_characters = set(phrase)

for char in sorted(unique_characters):
    print(f"{char}: {phrase.count(char)} time/s")