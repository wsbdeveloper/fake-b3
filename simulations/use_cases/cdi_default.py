
from decimal import Decimal
from unicodedata import name
from pyparsing import Char

from simulations.domain.cdi import TransactionCdi
from simulations.models import Simulations

class CdiDefault:
    def __init__(self, name: Char, invest: int, deadline: int) -> None:
        self.name = name
        self.invest = invest
        self.deadline = deadline

    def exec(self):
        try:
            transaction = TransactionCdi(name=self.name, invest=self.invest, deadline=self.deadline)
            simulation = transaction.helpersIpca.exec()

            Simulations.objects.create(
                name=simulation['name'],
                amount=simulation['amount'],
                cdi=simulation['percent_cdi'],
                irr=simulation['percent_irr'],
                rate=simulation['percent_rate']
            )

            return simulation
        except Exception as err:
            raise err

