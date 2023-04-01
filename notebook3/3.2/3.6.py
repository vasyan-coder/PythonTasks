def small_det(matrix):
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    return a * d - b * c


m = [[4, 3], [1, 1]]
print(small_det(m))
