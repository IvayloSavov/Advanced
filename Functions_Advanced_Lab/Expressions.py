import itertools
numbers = [n for n in input().split(", ")]
n = len(numbers)
permutations = itertools.product("-+", repeat=n)

for permutation in permutations:
    zipped = zip(permutation, numbers)
    expr = "".join(itertools.chain(*zipped))
    res = eval(expr)
    print(f"{expr}={res}")