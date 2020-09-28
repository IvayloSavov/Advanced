rows_count, columns_count = tuple(int(x) for x in input().split(", "))
matrix = []

for _ in range(rows_count):
    matrix.append([int(x) for x in input().split(" ")])

for col in zip(*matrix):
    print(sum(col))
