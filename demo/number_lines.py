import string

with open("text", "r") as file, open("output", "w") as output_fh:
    for i, line in enumerate(file):
        print(f"Line {i + 1}: {line.rstrip()} ({len([ch for ch in line if ch.isalpha()])})"
              f"({len([ch for ch in line if ch in string.punctuation])})", file=output_fh)
