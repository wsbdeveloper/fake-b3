from unicodedata import name


class Transaction:
    def __init__(self, name, amount, type_invest):
        self.name = name
        self.amount = amount,
        self.type_invest = type_invest

    @property
    def name(self):
        return self.name

    @property
    def amount(self):
        return self.amount

    @property
    def type(self):
        self.type_invest


