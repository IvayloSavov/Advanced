n = int(input())

names = set()

for _ in range(n):
    name = input()
    if name not in names:
        print(name)
        names.add(name)

# print("\n".join(set((input() for entry in range(int(input()))))))