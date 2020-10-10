def is_valid(index, element):
    return 0 <= index <= len(element) - 1


def get_magic_triangle(n):
    triangle = [[1], [1, 1]]
    rows_count = 2

    while rows_count < n:
        rows_count += 1
        current_row = []
        previous_row_index = rows_count - 2
        cols_count = rows_count
        for j in range(cols_count):
            f_element = 0
            s_element = 0
            if is_valid(j - 1, triangle[previous_row_index]) and is_valid(j, triangle[previous_row_index]):
                f_element = triangle[previous_row_index][j - 1]
                s_element = triangle[previous_row_index][j]

            elif is_valid(j - 1, triangle[previous_row_index]):
                f_element = triangle[previous_row_index][j - 1]

            elif is_valid(j, triangle[previous_row_index]):
                s_element = triangle[previous_row_index][j]

            new_element = s_element + f_element
            current_row.append(new_element)

        triangle.append(current_row)

    return triangle
    

print(get_magic_triangle(5))
