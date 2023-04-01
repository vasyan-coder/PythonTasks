def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


print(transpose([[0, 2, 1], [1, 0, 3], [0, 1, 1]]))
