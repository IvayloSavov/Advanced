from itertools import chain


def read_matrix():
    rows, cols = [int(n) for n in input().split(', ')]
    matrix = [
        [int(n) for n in input().split(', ')]
        for _ in range(rows)
    ]
    return matrix


def get_squares(matrix, size):
    squares = []
    for i in range(len(matrix) - (size - 1)):
        row = matrix[i]
        for j in range(len(row) - (size - 1)):
            square = [
                matrix[i + n][j:j + size]
                for n in range(size)
            ]
            squares.append(square)
    return squares


def get_sum_of_matrix(matrix):
    return sum(chain(*matrix))


def get_max_square(squares):
    """
    Sample Input:
    [
        [[1, 2], [3, 4]],
        [[3, 2], [3, 4]],
        [[5, 2], [3, 4]],
    ]
    """
    max_square_sum = None
    max_square = None
    for square in squares:
        square_sum = get_sum_of_matrix(square)
        if max_square_sum is None or square_sum > max_square_sum:
            max_square_sum = square_sum
            max_square = square
    return max_square


matrix = read_matrix()
squares = get_squares(matrix, 3)
max_square = get_max_square(squares)

print('\n'.join([' '.join(map(str, row)) for row in max_square]))
print(get_sum_of_matrix(max_square))