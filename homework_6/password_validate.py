'''Написать функцию, принимающую строку-пароль. Функция должна проверить подходит ли этот пароль условиям и вернуть True - если подходит; False - если не подходит. Условия:
Должен быть не менее 6 символов;
Должен содержать хотя бы одну цифру;
Не должен состоять только из цифр;
Не должен  содержать слово  “password” в любом регистре.'''


def password(data: str) -> bool:
    '''Функция проверки корректности пароля
        параметр data:
            пароль
        возвращается: если пароль прошел все условия проверки возварщается, истинна иначе ложь
    '''

    if len(data) < 6:
        return False
    if 'password' in data or data in 'PASSWORD':
        return False
    count_digit = 0
    for i in data:
        if i.isdigit():
            count_digit += 1
    if count_digit > 1 and count_digit != len(data):
        return True
    else:
        return False


# paswd = input('Введите пароль для проверки по заданным условиям - ')
#
# if password(paswd) == True:
#     print(f'Пароль подошел ко всем условиям и вывел истинну {password(paswd)}')
# elif password(paswd) == False:
#     print(f'Пароль не прошел заданные условия и вернул ложь {password(paswd)}')

# Если я все правильно понял , то пароль не должен содержать password и Password даже если
# пароль будет выглядеть вот так
# password123 123Password13
#  иначе если я в условии нужно его поменять на if data in 'password' or data in 'PASSWORD'