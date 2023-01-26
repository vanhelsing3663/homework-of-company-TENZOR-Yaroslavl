from random import randint

'''Заполнить два случайных набора чисел. Вывести оба набора. Указать какие элементы:
A) входят одновременно в оба;
B) входят только в первое, но не входят во второе;
C) входят только во второе, но не входят в первое;
D) входят в первое или во второе, но не в оба из них одновременно.'''

lenght_1 = randint(1, 20)
lenght_2 = randint(1, 20)
multiplicity_1 = {randint(1, 20) for i in range(lenght_1)}
multiplicity_2 = {randint(1, 20) for i in range(lenght_2)}
print(f'Два случайных набора различной длины :\n1) {multiplicity_1}\n2) {multiplicity_2}')

print(f'''A) Элементы которые входят в оба набора {multiplicity_1 & multiplicity_2}
B) Элементы которые входят только в первый набор , но не входят во второй {multiplicity_1 - multiplicity_2}
C) Элементы которые входят только во второй набор  но н е входят в первый {multiplicity_2 - multiplicity_1}
D) Элементы которые входят только в первое и второе , но не в оба одновременно {multiplicity_1 ^ multiplicity_2}''')

