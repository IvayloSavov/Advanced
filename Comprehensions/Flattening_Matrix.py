n = int(input())

matrix = [[int(n) for n in input().split(", ")] for _ in range(n)]
flat_matrix = [number for row in matrix for number in row]
print(flat_matrix)

# one liner
# print([int(n) for _ in range(int(input())) for n in input().split(", ")])

# Solving from another student

# size = int(input())
# matrix = [list(map(int, input().split(", ")))for _ in range(size)]
# l = [num for sublist in matrix
#      for num in sublist]
# print(l)
# ##################################
# from itertools import chain
# matrix = [list(map(int, input().split(", "))) for _ in range(int(input()))]
# m = list(t for t in chain(*matrix))
# print(m)