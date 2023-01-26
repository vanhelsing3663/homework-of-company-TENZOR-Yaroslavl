from random import randint

''' Сортировка методом пузырька '''

length = randint(5, 20)  # длина массива
arr = [randint(1, 1000) for num in range(length)]  # генератор рандомных чисел
arr2 = arr
print(f'1) Не отсортированный массив : {arr}')

print('#^#' * 30)
for i in range(length - 1):
    for j in range(length - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(f'2) Отсортированный массив :  {arr}')

length_2 = randint(5, 20)  # длина массива
arr_2 = [randint(1, 1000) for num in range(length_2)]  # генератор рандомных чисел
print('#^#' * 30)
print(f'3)Сортировка которая будет в обратном порядке исходный массив : {arr_2}')
for i in range(length_2 - 1):
    for j in range(length_2 - i - 1):
        if arr_2[j] < arr_2[j + 1]:
            arr_2[j], arr_2[j + 1] = arr_2[j + 1], arr_2[j]
            # print(arr) - вывод сортировки по шагам
print('#^#' * 30)
print(f'4) Сортировка в обратном порядке : {arr_2}')
