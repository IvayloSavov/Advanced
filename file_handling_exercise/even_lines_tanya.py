with open("1_text", "r") as file:
    for i, line in enumerate(file):
        if i % 2 == 0:
            for el in "-,.!?":
                line = line.replace(el, "@")
            words = reversed(line.split())
            print(" ".join(words))