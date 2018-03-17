import numpy as np

DAYS_OF_WEEK = 7
ITERATION_COUNT = 100000


# Простой способ прогнозирования
def simple(data, is_day=False):
    result = sum(data[len(data) - DAYS_OF_WEEK:])
    return result / DAYS_OF_WEEK if is_day else result


# Метод Эфрона
def efron(data, is_day=False):
    result = []
    for i in range(0, ITERATION_COUNT):
        var = sum(np.random.choice(data, size=DAYS_OF_WEEK))
        result.append(var / DAYS_OF_WEEK if is_day else var)
    return np.average(result)
