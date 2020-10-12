with open("text", "r") as file:
    ch_to_replace = {"-", ",", ".", "!", "?"}
    for i, line in enumerate(file):
        if i % 2 == 0:
            for ch in ch_to_replace:
                line = line.replace(ch, "@")
            line = line.split()[::-1]
            print(*line)
