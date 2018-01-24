import pandas as pd

# чтение из файла
# Все файлы, что нужно прочитать, дабы собрать с них данные
holidays_events = pd.read_csv('data/holidays_events.csv')
items = pd.read_csv('data/items.csv')
oil = pd.read_csv('data/oil.csv')
sample_submission = pd.read_csv('data/sample_submission.csv')
stores = pd.read_csv('data/stores.csv')
test = pd.read_csv('data/test.csv')
train = pd.read_csv('data/train.csv')
train2 = pd.read_csv('data/train2.csv')
transactions = pd.read_csv('data/transactions.csv')


#  Теперь стоило бы понять, что с этим всем делать :D

# так берёт каждый элемент по колонке
# for i in fixed_df['id']:
#     print(i)

# как выводить график пока не понятно
# fixed_df.plot()
