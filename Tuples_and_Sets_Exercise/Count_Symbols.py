def count_symbols(string):
    occurrences_of_character = dict()

    # /1 for ch in sorted(string):
    for ch in string:
        if ch not in occurrences_of_character.keys():
            occurrences_of_character[ch] = 0
        occurrences_of_character[ch] += 1

    # /1 return occurrences_of_character

    return dict(sorted(occurrences_of_character.items(), key=lambda ch_occurrence: ch_occurrence[0]))


def printing_the_final_result(dictionary):
    for ch, occurrence in dictionary.items():
        print(f'{ch}: {occurrence} time/s')


text = input()
occurrences_dict = count_symbols(text)
printing_the_final_result(occurrences_dict)