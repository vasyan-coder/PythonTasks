def submatrix(matrix, i, j):
    res = [row[0:j] + row[j + 1:] for row in (matrix[0:i] + matrix[i + 1:])]
    return res


matrix = [[0, 2, 1],
          [1, 4, 3],
          [2, 1, 1]]

print(submatrix(matrix, 1, 2))
