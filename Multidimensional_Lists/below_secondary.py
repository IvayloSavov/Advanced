def calculate_below_secondary_diagonal_sum(matrix):
    n = len(matrix)
    the_sum = 0
    for row in range(n):
        for col in range(n - row - 1, n):
            the_sum += matrix[row][col]
        return the_sum

def calculate_below_primary_diagonal_sum(matrix):
    n = len(matrix)
    the_sum = 0
    for row in range(n):
        for column in range(row + 1):
            the_sum += matrix[row][column]

    # or

    for row in range(n):
        for column in range(n):
            if row == column:  # if row < column
                break
            the_sum += matrix[row][column]


def calculate_between_the_two_diagonals_below(matrix):
    n = len(matrix)
    the_sum = 0
    for row in range(n):
        for column in range(n - 1 - row, row + 1):
            the_sum += matrix[row][column]