import datetime

from Data import TransactionHistory
import reader
import forecasting_methods as forecast
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

DAYS_OF_WEEK = 7
SHOPS_COUNT = 54


# Метод получения справочника магазинов
def get_shops(value):
    result = {}
    for i in range(1, SHOPS_COUNT + 1):
        data = value.loc[i]
        data.index = pd.to_datetime(data.date)
        result[i] = TransactionHistory(data)
    return result


def get_errors(shops, weak_day=''):
    simple_error = []
    efron_error = []
    for value in shops.values():
        last_weak = value.last_weak
        learning_history = value.learning_history

        if weak_day != '':
            last_weak = last_weak.query('weekday==' + weak_day)
            learning_history = learning_history.query('weekday==' + weak_day)

        correct_value = sum(last_weak.transactions)
        data = learning_history.transactions
        simple_error.append(MAPE(correct_value, forecast.simple(data, weak_day != '')))
        efron_error.append(MAPE(correct_value, forecast.efron(data, weak_day != '')))
    return simple_error, efron_error


def MAPE(correct_value, forecast_value):
    return abs(correct_value - forecast_value) / correct_value * 100


def show_histogram(data):
    data.plot()
    plt.show()


def show_bar(simple_error, efron_error):
    opacity = 0.8
    width = 0.3
    plt.bar(np.arange(len(simple_error)), simple_error, width, alpha=opacity, color='g', label='simple')
    plt.bar(np.arange(len(efron_error)) + width, efron_error, width, alpha=opacity, color='r', label='efron')
    plt.legend()
    plt.show()


# 2013-01-07
# 2017-08-13

if __name__ == '__main__':
    transactions = reader.get_transactions()
    transactions.sort_index()
    transactions = transactions.loc['2013-01-07':'2017-08-13']
    transactions = transactions.reset_index()
    transactions.index = transactions.store_nbr
    transactions['weekday'] = [datetime.datetime.strptime(x, '%Y-%m-%d').weekday() for x in transactions.date.values]

    shops = get_shops(transactions)
    # от 0 до 6 - пн - вс
    simple_error, efron_error = get_errors(shops)
    show_bar(simple_error, efron_error)
