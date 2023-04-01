def matrix_sum(matrix_a, matrix_b):
    matrix_sum = []
    for row_idx in range(len(matrix_a)):
        row_sum = []
        for col_idx in range(len(matrix_a[row_idx])):
            row_sum.append(matrix_a[row_idx][col_idx] + matrix_b[row_idx][col_idx])
        matrix_sum.append(row_sum)
    return matrix_sum


print(matrix_sum([[0, 2], [3, 0]], [[1, 4], [2, 0]]))
