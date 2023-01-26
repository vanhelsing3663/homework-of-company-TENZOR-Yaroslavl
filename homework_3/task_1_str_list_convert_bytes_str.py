'''Написать функцию преобразующую список строк , в список байт кодов. Написать обратную функцию'''
import ast


def string_list_conversion(lst):
    '''Функция возврата списка байткодов строк
    :param lst: в аргумент lst передается строка которая преобразуется в список с разбиением по пробелу
    :return: на выходе получаем список байт кодов списка строк
    '''
    byte_list = [bytes(i, encoding='utf-8') for i in lst]
    return byte_list


def bytes_list_conversion(letter):
    '''Функция преобразования списка байтов в список строк
    :param letter:  в аргумент letter передается результат функции string_list_conversion
    :return: возвращается список строк в привычном для юзера виде
    '''
    return [i.decode('utf-8') for i in letter]


def b(l):
    return [i.decode('utf-8') for i in l]


while True:
    flag = True
    while flag:

        try:
            number = int(input('''1)Введите 1 , чтобы преобразовать список строк в список байт кодов этих строк
2)Введите 2 , чтобы преобразовать список байт кодов строк из команды 1 в список строк в привычном для юзера вид
3)Введите 3, чтобы остановить программу
4)Введите 4, чтобы запустить программу с готовыми данными
5)Введите 5, чтобы ввести список байтов с клавиатуры например b'\\xd0\\xbf\\xd1\\x80\\xd0\\xb8\\xd0\\xb2\\xd0\\xb5\\xd1'
Пользовательский ввод :'''))
            if type(number) == int:
                if 1 <= number <= 5:
                    flag = False
                else:
                    raise ValueError
            else:
                raise NameError
        except NameError:
            print('Не вводите строковые значения')
        except ValueError:
            print('Введите числа в диапазоне от 1-3\n')
    if number == 1:
        arg_1 = string_list_conversion(list(map(str, input('Введите список строк через пробел : ').split())))
        arg_2 = bytes_list_conversion(arg_1)
        print(f'Список байт кодов строк {arg_1}\n')
    if number == 2:
        arg_1 = string_list_conversion(list(map(str, input('Введите список строк через пробел : ').split())))
        arg_2 = bytes_list_conversion(arg_1)
        print(f'Преобразованния из списка байт кодов в список строк в привычном для юзера виде : ')
        print(f'{arg_1} -> {arg_2}')
    if number == 3:
        break
    if number == 4:
        arg_1 = string_list_conversion('Привет как дела меня зовут Кирилл'.split())
        arg_2 = bytes_list_conversion(arg_1)
        print(f'Преобразованния из списка байт кодов в список строк в привычном для юзера виде : ')
        print(f'{arg_1} -> {arg_2}')
    if number == 5:
        lst = list(map(str, input('Введите список байт-кодов через запятую и пробел').split(', ')))
        byt = [ast.literal_eval(i) for i in lst]
        print(f'Список байтов: {byt}')
        dec = bytes_list_conversion(byt)
        print(f'Декодированый list : {dec}')
