import numpy as np

DAYS_OF_WEEK = 7
ITERATION_COUNT = 100


# Простой способ прогнозирования
def simple_forecast(data):
    return sum(data[len(data) - DAYS_OF_WEEK:])


# Метод Эфрона
def efron(data):
    result = []
    for i in range(0, ITERATION_COUNT):
        result.append(sum(np.random.choice(data, size=DAYS_OF_WEEK)))
    return np.average(result)
