import numpy
import time

last_starting = 0


def decorator_log_time_frequency(func):
    def wrapper(*args):
        global last_starting
        if time.time() - last_starting < 4:
            print('Ожидайте...')
            return 0
        with open('log.txt', 'a', encoding='utf-8') as file:
            file.write(f'{func.__name__}  Стартуем функцию ! \n')
            begin = time.time()
            result = func(*args)
            print(f'Время выполнения функции: {func.__name__} - {time.time() - begin}')
            file.write(f'{func.__name__} Фиииииииииииииииииииииинишь him) !!! \n')
        last_starting = time.time()
        return result

    return wrapper


@decorator_log_time_frequency
def random_function(c, d):
    a = numpy.random.sample((c, d))
    return a


mat = random_function(100, 1000)
mat = random_function(100, 1000)
time.sleep(4)
mat = random_function(100, 1000)
