import pandas as pd

# чтение из файла
fixed_df = pd.read_csv('data/test.csv')

# вывод колонки по имени
# fixed_df['id']

# так берёт каждый элемент по колонке
for i in fixed_df['id']:
    print(i)

# как выводить график пока не понятно
# fixed_df.plot()
