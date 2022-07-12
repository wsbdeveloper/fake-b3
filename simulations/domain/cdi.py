from black import err
from pyparsing import Char

from simulations.domain.helpers.cdi import HelpersCdi


class TransactionCdi:
    def __init__(self) -> None:
        self.helper_cdi = HelpersCdi()

    def exec(self):
        try:
            self.helper_cdi.exec()
        except Exception as err:
            raise err
