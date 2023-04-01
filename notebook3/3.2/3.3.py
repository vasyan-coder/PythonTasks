def dot(matrix1, matrix2):
    result = [[0 for x in range(len(matrix2[0]))] for y in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


print(dot([[1, 2], [3, 4], [5, 6]], [[1, 2, 3], [4, 5, 6]]))
