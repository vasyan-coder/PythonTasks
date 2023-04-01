def parse_equation(s, n):
    try:
        if len(s) == 3 or s[-1] == 'x':
            if s[-1] != 'x':
                return 0, s[2]
            else:
                k = s.replace('y=','').replace('*x','').strip()
                return k, 0
        k, b = s.split('+')
        k = k.replace('y', '').replace('x', '').replace('=', '').replace('*', '').strip()
        b = b.replace('y', '').replace('x', '').replace('=', '').strip()
        if k == '':
            k = 1
        elif k == '-':
            k = -1
        else:
            k = float(k)
        b = float(b)
        return k, b
    except:
        print(f"Прямая {n} неверна")
        return None


def is_parallel(eq1, eq2):
    try:
        k1, b1 = parse_equation(eq1, 1)
        k2, b2 = parse_equation(eq2, 2)
    except TypeError:
        return
    if k1 is None or k2 is None:
        return None
    elif k1 == k2:
        return True
    else:
        return False


eq1 = input('Введите уравнение первой прямой: ')
eq2 = input('Введите уравнение второй прямой: ')

parallel = is_parallel(eq1, eq2)
if parallel is None:
    print('Одно из уравнений введено неверно')
elif parallel:
    print('Прямые параллельны')
else:
    print('Прямые не параллельны')
