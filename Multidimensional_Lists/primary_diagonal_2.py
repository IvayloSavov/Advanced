n = int(input())
matrix = [[int(x) for x in input().split(" ")] for i in range(n)]
diagonal_sum = sum([matrix[i][i] for i in range(len(matrix))])
# diagonal_sum = 0

# for i in range(len(matrix)):
#     diagonal_sum += matrix[i][i]

print(diagonal_sum)