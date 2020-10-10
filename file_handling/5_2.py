import string

with open('word.txt') as file:
    words = file.read().split()

words_dict = {word.lower(): 0 for word in words}

with open('input.txt') as file:
    for line in file:
        new_line = ''
        for ch in line.lower():
            new_line += ' ' if ch in string.punctuation else ch
        new_line_list = new_line.split()
        for word in words_dict:
            words_dict[word] += new_line_list.count(word)


words_dict = dict(sorted(words_dict.items(), key=lambda x: -x[1]))
with open('output.txt', 'w') as file:
    for k, v in words_dict.items():
        file.write(f'{k} - {v}\n')