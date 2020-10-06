f = open("numbers.txt", "r")
total = 0
for line in f:
    n = int(line.strip())
    total += n
print(total)

# print([sum([int(line.strip())]) for line in open("numbers.txt", "r")])