traffic_information = """Выбор движения персонажа
                         1 - вперед, 2 - назад, 3 - вправо, 4 - влево
                         стоп - выход\n"""
man_steps = "Введите целое не отрицательное число : "
x = y = 0


def move_human(x):
    """Функция получает количество ходов от пользователя
            и проверяет это число
    аргументы:
            целое число  x

    возвращает:
        Целое число ходов.
        0, если пользователь ошибся
    """
    step = int(input(x))
    if step >= 0:
        return step
    else:
        print('Число < 0')
        return 0


while True:
    err = False
    print(f'Позиция человека: {x, y}')
    enter_where_to_go_man = input(f'{traffic_information}Введите число : ')
    match enter_where_to_go_man:
        case '1':
            x += move_human(f'Вперед! {man_steps}')
        case '2':
            x -= move_human(f'Назад! {man_steps}')
        case '3':
            y += move_human(f'Вправо! {man_steps}')
        case '4':
            y -= move_human(f'Влево! {man_steps}')
        case 'стоп':
            print('Движение окончено')
            break
        case _:
            err = True
            print('Введите корректные данные')
    if not err:
        print(f'Персонаж остановился в точке : {x, y}')
