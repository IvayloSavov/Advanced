with open("1_text", "r") as text:
    text_input = text.readlines()

ch_to_change = {"-", ",", ".", "!", "?"}

for i, line in enumerate(text_input):
    if i % 2 == 0:
        new_line = ""
        for ch in line:
            if ch in ch_to_change:
                ch = "@"
            new_line += ch
        new_line = new_line.split()
        new_line.reverse()
        print(*new_line)