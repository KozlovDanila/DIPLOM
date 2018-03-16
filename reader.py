import pandas as pd


def get_holidays_events():
    return pd.read_csv('data/holidays_events.csv')


def get_items():
    return pd.read_csv('data/items.csv')


def get_oil():
    return pd.read_csv('data/oil.csv')


def get_stores():
    return pd.read_csv('data/stores.csv')


def get_test():
    return pd.read_csv('data/test.csv')


def get_train():
    return pd.read_csv('data/train.csv')


def get_train2():
    return pd.read_csv('data/train2.csv')


def get_transactions():
    return pd.read_csv('data/transactions.csv', index_col='date')
