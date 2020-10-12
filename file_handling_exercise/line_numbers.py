with open("2_text", "r") as file, open("output_fh", "w") as output_fh:
    result_text = ""
    for i, line in enumerate(file):
        length = len([el for el in line if el.isalpha()])
        counter = 0
        for el in line:
            if el in "',.!?\";:-":
                counter += 1
        # print(f"Line {i + 1}: {line[:-2]} ({length})({counter})", file=output_fh)
        result_text += f"Line {i + 1}: {line[:-2]} ({length})({counter})\n"

print(result_text)
# with open("output", "w") as file:
#     file.write(result_text)
