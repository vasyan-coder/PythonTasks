import numpy as np


def levenshtein_distance(a, b, i=0, j=0):
    if i == 0 or j == 0:
        return max(i, j)
    elif a[i - 1] == b[j - 1]:
        return levenshtein_distance(a, b, i - 1, j - 1)
    else:
        return 1 + min(min(levenshtein_distance(a, b, i, j - 1), levenshtein_distance(a, b, i - 1, j)),
                       levenshtein_distance(a, b, i - 1, j - 1))


def lev_dist_ops(s1, s2):
    d = np.zeros((len(s1) + 1, len(s2) + 1))

    # Populate the matrix
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0:
                d[i][j] = j
            elif j == 0:
                d[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = 1 + min(d[i][j - 1],
                                  d[i - 1][j],
                                  d[i - 1][j - 1])

    ops = []
    i = len(s1)
    j = len(s2)

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            i -= 1
            j -= 1
        elif d[i - 1][j] < d[i][j]:
            ops.append("удаление")
            i -= 1
        elif d[i][j - 1] < d[i][j]:
            ops.append("вставка")
            j -= 1
        else:
            ops.append("замена")
            i -= 1
            j -= 1

    while i > 0:
        ops.append("удаление")
        i -= 1

    while j > 0:
        ops.append("вставка")
        j -= 1

    ops.reverse()
    return ops


print(lev_dist_ops('слон', 'слоны'))
