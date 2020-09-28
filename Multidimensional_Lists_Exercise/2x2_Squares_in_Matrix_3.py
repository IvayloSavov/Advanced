M, N = tuple(map(int, input().split(" ")))

matrix = [["a"] * N for i in range(N)]

num_squares = 0

for i in range(M):
    row = input().split(" ")
    for j in range(N):
        matrix[i][j] = row[j]

        if i - 1 >= 0 and j - 1 >= 0:
            if matrix[i][j] == matrix[i][j - 1] and matrix[i][j] == matrix[i - 1][j] and matrix[i][j] == matrix[i - 1][j - 1]:
                num_squares += 1

print(num_squares)
