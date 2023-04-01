def small_det(matrix):
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    return a * d - b * c


def submatrix(matrix, i, j):
    res = [row[0:j] + row[j + 1:] for row in (matrix[0:i] + matrix[i + 1:])]
    return res


def det_matrix(a):
    n = len(a)
    if n == 1:
        return a[0][0]
    else:
        sum_det = 0
        for c in range(len(a)):
            if len(submatrix(a, 0, c)[0]) == 2:
                sum_det += ((-1) ** c) * a[0][c] * small_det(submatrix(a, 0, c))
            else:
                sum_det += ((-1) ** c) * a[0][c] * det_matrix(submatrix(a, 0, c))
        return sum_det


matrix = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1],
]
print(det_matrix(matrix))
