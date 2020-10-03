line = input().split()
filtered = [word for word in line if len(word) % 2 == 0]
print("\n".join(filtered))

[print(word) for word in input().split() if len(word) % 2 == 0]