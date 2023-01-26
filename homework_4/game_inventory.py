from pprint import pprint  # модуль для читаемого вывода словаря

'''
Игровой инвентарь
Инструкции
1)Инвентарь не должен весить < 20 кг
2)Из инвентаря можно выбрасывать предметы
3)Так же в инвентарь можно брать предметы у Сидоровича
'''

print(f'''Эй! Иди сюда, подкину тебе кое-чего!
Меченный, взгляни что для тебя есть''')
print()
inventory_gun = {'Пистолет Пмм': 0.7,
                 'Пистолет Черный ястреб': 0.6,
                 'Дробовик Обрез':  1.5,
                 'Автомат Акм-74/2y': 3,
                 'Автомат Гром-С13': 5,
                 'Спецавтомат "ВЛА"': 4,
                 'Винтовка Винтарь-ВС': 4.5,
                 'Винтовка СВУмк-2': 5,
                 'Винтовка СВДм-2': 5,
                 'Гранатомет РПГ-7у': 11,
                 'Гранатомет Бульдог-6': 12}

inventory_help = {'Бинт': 0.22,
                  'Антирад': 0.32,
                  'Аптечка малая': 0.9,
                  'Аптечка Большая': 1.5,
                  'Броня (шлем)': 1,
                  'Бронежелет': 2.5,
                  'Бронежелет и шлем': 3.5}

pprint(inventory_help)
pprint(inventory_gun)
print()
print(f'''Я тебя спас и в благородство играть не буду. 
Выполнишь для меня пару заданий — и мы в расчёте.
Заполни свой инвентарь, чтобы не идти в зону пустым!
Смотри , чтобы инвентарь не переполнило специально для тебя сколько весит подписал...''')
print()

inventory_dictionary = dict()

while True:
    subject = input('''Меченный выбирай
    1)Нажми 1 , чтобы добавить в инвентарь оружие или 1.1 , чтобы добавить медикаменты
    1.1)Нажми 1.1 ,чтобы добавить медикаменты
    2)Нажми 2 , чтобы удалить предмет из инвентаря
    3)Нажми 3 , чтобы посмотреть инвентарь и узнать его вес
    4)Нажми 4 , чтобы поблагодарить Сидоровича и выйти
    Вводи:''')
    if subject == '1':
        try:
            gun = input('Вводи какое оружие хочешь добавить: ')
            inventory_dictionary[gun] = inventory_gun[gun]
            print(f'Сейчас в твоем инвентаре {inventory_dictionary}')
        except Exception as e:
            print('Ну что ты там ввел давай по новой!')
    if subject == '1.1':
        try:
            medecine = input('Введи чем будешь лечиться : ')
            inventory_dictionary[medecine] = inventory_help[medecine]
        except Exception as e:
            print('Ну что ты там ввел давай по новой!')
    if subject == '2':
        try:
            print(f'Предметы {inventory_dictionary}')
            drop = input('Введи , что хочешь удалить : ')
            del inventory_dictionary[drop]
        except Exception as e:
            print('Удаляй только то что есть в инвентаре')
    if subject == '3':
        if sum(inventory_dictionary.values()) < 20:
            print(
                f'''Вот что набрал {inventory_dictionary} . Вес твоего инвентаря составляет : {sum(inventory_dictionary.values())} кг''')
        else:
            print(
                f'Вот что набрал {inventory_dictionary} . Выброси что-нибудь слишком много предметов: {sum(inventory_dictionary.values())} кг')
    if subject == '4':
        print('Спасибо, Сидорович, до встречи!')
        break
    if sum(inventory_dictionary.values()) > 20:
        break
if sum(inventory_dictionary.values()) > 20:
    print(f'Собери инвентарь заново ты не унесешь {sum(inventory_dictionary.values())}')
else:
    print(f'Уххх, в моем инвентаре теперь:')
    s = ''
    for item, kg in inventory_dictionary.items():
        s += f'{item}-{kg}кг,'
    print(s[:-1])
    print(f'Спасибо Сидоровичу , что не дал взять больше всего лишь {sum(inventory_dictionary.values())} кг\n'
          f'Выдвигаюсь в зону')
