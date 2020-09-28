import itertools


def read_matrix():
    rows, cols = [int(n) for n in input().split(", ")]
    matrix = [[int(number) for number in input().split(", ")] for _ in range(rows)]

    return matrix


def get_squares(matrix):
    squares = []
    for i in range(len(matrix) - 1): # за да не излезем извън матрицата
        row = matrix[i]
        for j in range(len(row) - 1):
            square = [
                [matrix[i][j], matrix[i][j + 1]],  # matrix[i][j:j+2]
                [matrix[i + 1][j], matrix[i + 1][j + 1]]  # matrix[i + 1][j:j+2]
            ] # три измерна, защото пазим матрици
    return squares


def get_sum_of_matrix(matrix):
    return sum(itertools.chain(*matrix))


def get_max_square(squares):
    max_square_sum = None
    max_square = None

    for square in squares:
        square_sum = get_sum_of_matrix(square)
        if max_square_sum is None or square_sum > max_square_sum:
            max_square_sum = square_sum
            max_square = square
    return max_square


matrix = read_matrix()
squares = get_squares(matrix)
max_square = get_max_square(squares)
print('\n'.join([' '.join(map(str, row)) for row in max_square]))
print(get_sum_of_matrix(max_square))
