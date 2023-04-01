def levenshtein_distance(a, b, i=0, j=0):
    if i == 0 or j == 0:
        return max(i, j)
    elif a[i - 1] == b[j - 1]:
        return dist(a, b, i - 1, j - 1)
    else:
        return 1 + min(min(levenshtein_distance(a, b, i, j - 1), levenshtein_distance(a, b, i - 1, j)),
                       levenshtein_distance(a, b, i - 1, j - 1))
