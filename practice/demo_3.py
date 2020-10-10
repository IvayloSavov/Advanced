with open("text.txt", "r") as text, open("words.txt") as words:
    words_count = {}
    lines = words.readlines()
    for line in lines:
        line = line.split()
        for word in line:
            words_count[word] = 0

    lines = text.readlines()
    for line in lines:
        line = line.replace("-", "")
        line = line.replace(".", "")
        line = line.replace(",", "")
        line = line.split()
        for word in line:
            if word in words_count.keys():
                words_count[word] += 1

    print(words_count)
