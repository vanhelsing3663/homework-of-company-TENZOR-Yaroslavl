'''XOR шифрование/расшифрование. На входе файл с текстом и ключ шифрования (строка),
на выходе преобразованное (зашифрованное/расшифрованное) сообщение в файле'''


def encrypt(text: str, key_1: str) -> str:
    '''Функция шифрования
    :param text:текст
    :param key: ключ шифрования
    :return: возвращаем строку в зашифрованном виде
    '''
    encrypted_text = ''
    for i in range(len(text)):
        a = ord(text[i])
        b = ord(key_1[i % len(key_1)])
        encrypted_text += chr(a ^ b)
    return encrypted_text


while True:
    flag = True
    while flag:

        try:
            number = int(input('''
                1-Шифрование текста
                2-Расшифрование текста
                3-Выход из программы
                Ввод :'''))
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
        with open("open.txt", "r") as open_file, open("crypt.txt", "w") as encrypted_file:
            key = input('Введите ключ для шфирования: ')
            open_text = open_file.read()
            encrypted_text = encrypt(open_text, key)
            encrypted_file.write(encrypted_text)
            print('Результат в crypt.txt')

    if number == 2:
        with open("crypt.txt", "r") as encrypted_file, open("decrypt.txt", "w") as decrypted_file:
            key = input('Введите ключ : ')
            encrypted_text = encrypted_file.read()
            decrypted_text = encrypt(encrypted_text, key)
            decrypted_file.write(decrypted_text)
            print('Результат в decrypt.txt')

    if number == 3:
        print('Выход из программы')
        break
