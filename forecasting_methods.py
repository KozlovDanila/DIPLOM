import random
import numpy as np

DAYS_OF_WEEK = 7


# Бутсраповский метод Эфрона.
def bootstrap_efron(data):
    result = []
    for i in range(100000):
        result.append(get_sum(get_pre_result(data)))
    return get_sum(result)


# Идём по всему массиву с данными, берём рандомный элемент из недели и добавляем в результат
def get_pre_result(data):
    pre_resulting = []
    len_data = len(data)
    for start in range(0, len_data, DAYS_OF_WEEK):
        end = DAYS_OF_WEEK + start - 1
        if end > len_data: break
        pre_resulting.append(data[random.randint(start, end)])
    return pre_resulting


# берём данные, суммируем и делим на длину(На длину ли нужно делить?)
def get_sum(data):
    return np.sum(data) / len(data)
