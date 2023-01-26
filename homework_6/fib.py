''' Написать функцию, которая возвращает заданное число Фибоначчи. Обязательно через рекурсию.'''


def fibonacci(n):
    '''Функция
         параметр n:
            число которое больше 0
        возвращает:
            число Фиббоначи
    '''
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# try:
#     number_1 = int(input('Введите число - '))
#     if number_1 < 0:
#         raise RecursionError
#     else:
#         print(f'Результат {fibonacci(number_1)}')
#
# except ValueError:
#     print('не вводите строковые значения')
# except RecursionError:

#     print('Введите значение > 0')