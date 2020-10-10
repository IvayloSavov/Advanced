import itertools
permutations = itertools.product(["+"], ["-"], repeat=5)
print(list(permutations))