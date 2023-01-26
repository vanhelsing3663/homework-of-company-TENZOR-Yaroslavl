def numbers_sum(x, y):
    '''Сумма двух чисел
    Принимает:
        x - первое число
        y - второе число
    Возвращает:
        Сумму чисел x и y
    '''
    try:
        if (type(x) and type(y)) in (float, int):
            return x + y
        else:
            return 'Не корректные данные'
    except Exception:
        return 'Некорректные данные'


def numbers_subtraction(x, y):
    '''Разность двух чисел
    Принимает:
        x - первое число
        y - второе число
    Возвращает:
        Разность чисел x и y
    '''
    try:
        if (type(x) and type(y)) in (float, int):
            return x - y
        else:
            return 'Не корректные данные'
    except Exception:
        return 'Некорректные данные'


def lengnt_subsequence(x):
    '''Длина последовательности
    Принимает:
        x - последовательность
    Возвращает:
        Длину последовательности
    '''
    return len(x)


def generate_list(x):
    '''Генерация списка
    Принимает:
        x - число для генерации последовательности
    Возвращает:
        Список
    '''
    try:
        if type(x) == int:
            return [i for i in range(x)]
        else:
            return 'Не корректные данные'
    except Exception:
        return 'Некорректные данные'