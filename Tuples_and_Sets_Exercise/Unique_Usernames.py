n = int(input())

names = set()

for _ in range(n):
    name = input()
    names.add(name)

print("\n".join(names))


# print("\n".join({input() for _ in range(int(input()))}))