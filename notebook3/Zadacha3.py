# Функция для вычисления количества проверочных битов
def check_bits(m):
    n = 0
    while 2 ** n <= m + n + 1:
        n += 1
    return n







def result(m):
    m = m[::-1]
    return map(str, m[1:])


# Функция для получения значения бита
def get_bit(data, i):
    mask = 1 << i
    return (data & mask) != 0


def hamming_code(data):
    data = int(data, 2)
    # Вычисляем количество проверочных битов для текущего числа
    n = check_bits(len(bin(data)) - 2)

    # создаем новый массив нулей
    code = [0] * (n + len(bin(data)) - 2)

    # заполняем код хэмминга
    for i in range(len(code)):

        # является ли текущий бит проверочным
        if 2 ** i & (2 ** i - 1):
            continue

        # обрабатываем текущий бит
        for j in range(len(code)):
            if get_bit(i + 1, j):
                code[i] ^= get_bit(data, j)

    # Возвращаем результат
    return ''.join(result(code))


# 0110011
data = "1011"
print(hamming_code(data))
