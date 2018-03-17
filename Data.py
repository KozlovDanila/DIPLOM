DAYS_OF_WEEK = 7


class TransactionHistory(object):
    def __init__(self, data):
        length = len(data)
        self.learning_history = data[:length - DAYS_OF_WEEK]
        self.last_weak = data[length - DAYS_OF_WEEK:]
