import random
import numpy as np


def scalar_product(X, Y):
    assert len(X) == len(Y), 'Векторы должны быть одной размерности'
    sp = 0
    for x, y in zip(X, Y):
        sp += x * y
    return sp


vector_len = int(input('Введите размерность векторов: '))
X = [random.randint(-10, 10) for i in range(vector_len)]
Y = [random.randint(-10, 10) for i in range(vector_len)]

print('Скалярное произведение векторов: ', scalar_product(X, Y))

assert scalar_product(X, Y) == np.dot(X, Y), 'Неверное значение скалярного произведения'
print('Проверка пройдена успешно!')

s = '123'
print(s[-1])