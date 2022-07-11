from decimal import Decimal
from pyparsing import Char

from transactions.domain.helpers.ipca import HelpersIpca

class TransactionIpca:
    def __init__(self, invest: Decimal, name: Char, deadline: int) -> None:
        self.helpersIpca = HelpersIpca(invest=invest, name=name, deadline=deadline)
