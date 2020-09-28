def find_symbol(matrix, symbol):
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == symbol:
                return i, j


n = int(input())
matrix = [list(input()) for _ in range(n)]
symbol = input()
result = find_symbol(matrix, symbol)

if result:
    print(result)
else:
    print(f"{symbol} does not occur in the matrix")