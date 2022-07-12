from decimal import Decimal
from pyparsing import Char

from simulations.domain.helpers.ipca import HelpersIpca

class TransactionIpca:
    def __init__(self, invest: int, name: Char, deadline: int) -> None:
        self.helpersIpca = HelpersIpca(invest=invest, name=name, deadline=deadline)
