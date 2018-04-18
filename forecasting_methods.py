import random

import numpy as np

DAYS_OF_WEEK = 7
ITERATION_COUNT = 100000


# Простой способ прогнозирования
def simple(data, is_day=False):
    result = sum(data[len(data) - DAYS_OF_WEEK:])
    return result / DAYS_OF_WEEK if is_day else result


# Метод Эфрона
def efron(data, is_day=False, is_smooth=False):
    data = list(data)
    if is_smooth:
        data = smooth(data)
    result = []
    for i in range(0, ITERATION_COUNT):
        var = sum(np.random.choice(data, size=DAYS_OF_WEEK))
        result.append(var / DAYS_OF_WEEK if is_day else var)
    return np.average(result)


# СГЛАЖИВАНИЕ
# 1. Сортируем
# 2. Высчитываем вероятность. Можно по каждому числу, но будет дурацкая вероятность
#    Можно по диапозону чисел. Буду по диапозону чисел, тк так будут большие вероятности.
#    Чтобы понять какой диапозон, беру самое маленькое число и самое большое, (max-min)/len(data). Что-то вроде кластера
#    И идти с этим дипозонам по значениям. То есть вероятность выпадения значения из данного диапозона такая-то
# 3. Вытаскиваем по вероятности числа из data.
# 4. Берём интервал с вероятность 1 - p и заполняем a+(b-a)*r

def smooth(data):
    copy_array = np.copy(list(data))
    copy_array.sort()
    data_range = get_data_range(copy_array)
    probability = get_probability(copy_array, data_range)
    for key in probability:
        if list(probability)[len(probability) - 1] == key: break
        a, b = get_interval(copy_array, key)
        data.append(round(a + (b - a) * random.random()))
    return data


def get_data_range(data):
    return np.math.ceil((max(data) - min(data)) / len(data))


def get_probability(data, data_range):
    result = {}
    temp_range = data[0] + data_range
    length = len(data)
    start = 0
    for i in range(length):
        if data[i] > temp_range:
            result[temp_range] = (i - start) / length
            start = i
            temp_range = data_range + data[i]
    result[temp_range] = (length - start) / length
    return result


def get_interval(data, value):
    i = 0
    while True:
        if data[i] > value:
            return data[i - 1], data[i]
        i += 1
