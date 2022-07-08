from distutils.log import error
from black import err
from transactions.domain.transaction import Transaction
from transactions.app.exceptions.transactionException import TransactionException404
from transactions.models import TransactionsModel


class CreateTransaction(Transaction):
    def __init__(self, name, amount, type_invest):
        super().__init__(name, amount, type_invest)

    def exec(transaction : Transaction):
        try:
            TransactionsModel.objects.create(transaction)
        except (TransactionsModel.DoesNotExist, TransactionException404) as erro:
            raise erro
