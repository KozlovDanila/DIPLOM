import random

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

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


if __name__ == '__main__':
    # Чтобы проанализировать данные, нужно либо собрать все данные в одно единое целое и понять как они взаимосвязанны,
    #  либо переводить из одной систему в другую(Напрмиер, в stores есть type, это буква, которую можно заменить на цифру
    # и тогда можно будет построить гистограмму)

    # Во многих таблицах есть какое-то одно место или один товар и по нему данные. И, возможно, дата.
    # Это наводит на мысль, что можно отсортировать по товару и смотреть исключительно его данные.
    # Насколько это верно?

    # чтение из файла
    # Все файлы, что нужно прочитать, дабы собрать с них данные
    # holidays_events = pd.read_csv('data/holidays_events.csv')
    # holidays_events.plot(kind='barh', y="locale_name", x="date")
    # items = pd.read_csv('data/items.csv')
    # oil = pd.read_csv('data/oil.csv')
    # stores = pd.read_csv('data/stores.csv')
    # test = pd.read_csv('data/test.csv')
    # train = pd.read_csv('data/train.csv')
    # train2 = pd.read_csv('data/train2.csv')
    transactions = pd.read_csv('data/transactions.csv')

    #  Теперь стоило бы понять, что с этим всем делать :D

    # так берёт каждый элемент по колонке
    # for i in fixed_df['id']:
    #     print(i)

    # Рисование гистограммы
    # plt.hist(stores['cluster'], 30)
    # plt.show()

    # Каждый 7 в 1 магазине произведено транзакций меньше. Удалять ли эти данные?
    only_1_store = transactions[transactions.store_nbr == 1]
    # удалим последнюю неделю
    last_week_1_store = only_1_store[len(only_1_store) - DAYS_OF_WEEK:]
    avg = np.sum(last_week_1_store.transactions) / DAYS_OF_WEEK
    print(avg)  # получается 1278.0
    print(bootstrap_efron(np.array(only_1_store.transactions)))  # получается 1524.544820920502 с 10 тысячими итераций
    # 1524.2368031380752 c 100 тысчими итераций
