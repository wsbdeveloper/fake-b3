
from decimal import Decimal
from unicodedata import name
from pyparsing import Char

from transactions.domain.ipca import TransactionIpca
from transactions.models import Transactions

class IpcaDefault:
    def __init__(self, name: Char, invest: Decimal, deadline: int) -> None:
        self.name = name
        self.invest = invest
        self.deadline = deadline

    def exec(self):
        try:
            transaction = TransactionIpca(name=self.name, invest=self.deadline, deadline=self.deadline)
            simulation = transaction.helpersIpca.exec()

            Transactions.objects.create(
                name=simulation['name'],
                amount=simulation['amount'],
                ipca=simulation['percent_ipca'],
                irr=simulation['percent_irr'],
                rate=simulation['percent_rate']
            )


            return simulation
        except Exception as err:
            raise err

