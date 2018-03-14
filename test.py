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
        length = len(data)
        result[i] = TransactionHistory(data[:length - DAYS_OF_WEEK], data[length - DAYS_OF_WEEK:])
    return result


def get_errors(shops):
    simple_error = []
    efron_error = []
    for value in shops.values():
        correct_value = sum(value.last_weak.transactions)
        data = value.learning_history.transactions
        simple_error.append(abs(correct_value - forecast.simple_forecast(data)))
        efron_error.append(abs(correct_value - forecast.efron(data)))
    return simple_error, efron_error


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


if __name__ == '__main__':
    transactions = reader.get_transactions()
    shops = get_shops(transactions)
    simple_error, efron_error = get_errors(shops)
    show_bar(simple_error, efron_error)


# Данные заканчиваются в середине недели.
# То есть если брать просто последние 7 дней из данных, это две половинчатые недели.

# shops[1].last_weak.index = pd.to_datetime(shops[1].last_weak.date)
# print(shops[1].last_weak.resample('W')['transactions'].mean())
# print(shops[1].last_weak.date)
