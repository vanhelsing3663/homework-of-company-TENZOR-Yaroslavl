from matplotlib import colors
from pprint import pprint  # модуль для читаемого вывода словаря

'''
Создать словарь цветов, в котором ключ - название или кодировка цвета;
значение - кортеж из rgb этого цвета.
'''

color_dictionary = {'Crimson': (220, 20, 60),
                    'Red': (255, 0, 0),
                    "Pink": (255, 192, 203),
                    'Yellow': (255, 255, 0),
                    'Green': (0, 128, 0),
                    'White': (255, 255, 255),
                    'SteelBlue': (70, 130, 180),
                    'Blue': (0, 0, 255),
                    'Silver': (192, 192, 192)}
print(f'Созданный словарь из ключа (цвет) :  значение (его RGB) -')
pprint(color_dictionary)

'''Еще я воспользовался библиотекой matplotlib и создал словарь с RGB  для тренировки и расширения кругозора'''

print()
info = '''1)Введите название цвета на Английском
2)Не используйте цифры
3)Для остановки программы введите "стоп"
Ввод : '''
color_name = input(info)
dictionary = {}
while True:
    if color_name != 'стоп':
        dictionary[color_name] = colors.to_rgb(color_name)
    if color_name == 'стоп':
        break
    if color_name.isdecimal() or color_name.isdigit():
        raise ValueError('Введите цвета на английском не используя числа')
    color_name = input('Ввод : ')
print(f'Созданный словарь из ключа (цвет) : значение (его RGB) - {dictionary}')

#
