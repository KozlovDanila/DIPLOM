import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter


# Чтобы проанализировать данные, нужно либо собрать все данные в одно единое целое и понять как они взаимосвязанны,
#  либо переводить из одной систему в другую(Напрмиер, в stores есть type, это буква, которую можно заменить на цифру
# и тогда можно будет построить гистограмму)

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
# transactions = pd.read_csv('data/transactions.csv')

#  Теперь стоило бы понять, что с этим всем делать :D

# так берёт каждый элемент по колонке
# for i in fixed_df['id']:
#     print(i)

# Рисование гистограммы
# plt.hist(stores['cluster'], 30)
# plt.show()


