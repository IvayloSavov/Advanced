def find_symbol(matrix, symbol):
    n = len(matrix)
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == symbol:
                return (row, col)

    return None


n = int(input())
matrix = []

for _ in range(n):
    line = list(input())
    matrix.append(line)

symbol = input()
result = find_symbol(matrix, symbol)

if result:
    print(result)
else:
    print(f"{symbol} does not occur in the matrix")