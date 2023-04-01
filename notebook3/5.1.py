def ham_dist(a, b):
    result = 0
    for i in range(len(bin(a)) - 2):
        if (a >> i) & 1 != (b >> i) & 1:
            result += 1
    return result