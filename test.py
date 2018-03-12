from Data import TransactionData, TransactionHistory
import reader

DAYS_OF_WEEK = 7


# Метод получения справочника магазинов
def get_shops(value):
    shops = {}
    for i in range(value.__len__()):
        string_data = value.loc[i]
        store_nbr = string_data.store_nbr
        if store_nbr in shops:
            shops[store_nbr].append(TransactionData(string_data.date, string_data.transactions))
        else:
            data = [TransactionData(string_data.date, string_data.transactions)]
            shops[store_nbr] = data
    result = {}
    for key, value in shops.items():
        result[key] = TransactionHistory(value[: len(value) - DAYS_OF_WEEK], value[len(value) - DAYS_OF_WEEK:])
    return result


if __name__ == '__main__':

    transactions = reader.get_transactions()
    shops = get_shops(transactions)
    for i in shops[1].last_weak:
        print(i.date, i.transaction_count)
