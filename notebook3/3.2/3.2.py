def multiply(A, B):
    C = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(B)):
                sum += A[i][k] * B[k][j]
            row.append(sum)
        C.append(row)
    return C


print(multiply([[0, 2], [3, 0]], [[1, 4], [2, 0]]))
