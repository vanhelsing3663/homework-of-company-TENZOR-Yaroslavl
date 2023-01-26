import numpy as np
from random import randint

arr = np.array([[randint(1, 1000) for step in range(3)], [randint(1, 1000) for step2 in range(3)],
                [randint(1, 1000) for step3 in range(3)]])
print('Результат создания массива  3 x 3 с рандомными числами : ')
print(arr)
arr_transpon = arr.transpose()
print('Результат Транспонирования матрицы : ')
print(arr_transpon)