from itertools import product, chain

numbers = input().split(", ")
n = len(numbers)
permutations = product("+-", repeat=n)

for perm in permutations:
    zipped = list(zip(perm, numbers))
    expr = "".join(chain(*zipped))
    res = sum(map(lambda z: int(z[1]) if z[0] == "+" else -int(z[1]), zipped))
    print(f"{expr}={res}")