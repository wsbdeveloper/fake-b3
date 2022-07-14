from black import err
from pyparsing import Char

from simulations.domain.helpers.cdi import HelpersCdi


class TransactionCdi:
    def __init__(self, invest: int, name: Char, deadline: int) -> None:
        self.helpersIpca = HelpersCdi(invest=invest, name=name, deadline=deadline)
