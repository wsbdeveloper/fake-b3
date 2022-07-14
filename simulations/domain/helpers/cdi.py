import os
from datetime import date
from dateutil.relativedelta import relativedelta
from pyparsing import Char


SELIC = os.getenv('SELIC', 9.25)
MULT_SELIC = os.getenv('MULT_SELIC', 0.98)
PERCENT_CDI = os.getenv('CDI_DEFAULT', 6)
PERCENT_IRR = os.getenv('CDI_IRR', 0.85)
PERCENT_RATE = os.getenv('CDI_RATE', 1.16)

class HelpersCdi:
    def __init__(self, invest: int, name: Char, deadline: int) -> None:
        self.invest = invest
        self.name = name
        self.deadline = deadline


    @property
    def selic(self):
        return SELIC / 100

    @property
    def taxa_contract_cdi(self):
        return  PERCENT_RATE / 100

    @property
    def summation(self):
        return (self.selic * MULT_SELIC) * self.taxa_contract_cdi

    @property
    def cdi(self):
        return (self.summation * 100) + 1

    @property
    def taxa_cdi(self):
        return self.cdi ** (1 / 12)

    def cdi_simulation(self, contribution: int) -> int:
        return contribution * self.taxa_cdi

    def total_cdi_simulation_result(self, contribution: int) -> int:
        return self.cdi_simulation(contribution=contribution) - contribution

    def patrymony_with_taxes(self, contribution: int) -> int:
        return self.total_cdi_simulation_result(contribution=contribution) * PERCENT_IRR

    def exec(self):
        try:
            amount = []
            aux_calcule = 0

            date_id = date.today() + relativedelta(months=1)
            aux_calcule = self.cdi_simulation(contribution=self.invest)
            income_ir = self.patrymony_with_taxes(contribution=self.invest)
            income_gross = self.total_cdi_simulation_result(
                contribution=self.invest
            )

            amount.append(
                {
                    'amount': format(aux_calcule, '.2f'),
                    'gross_ir': format(income_ir, '.2f'),
                    'income_gross': format(income_gross, '.2f'),
                    'date': date_id.strftime('%d/%m/%Y'),
                }
            )

            for data in range(1, self.deadline):
                date_id = date.today() + relativedelta(months=data + 1)
                # patrimonio total
                aux_calcule = self.cdi_simulation(contribution=aux_calcule)

                # rendimento com imposto
                income_ir = self.patrymony_with_taxes(contribution=aux_calcule)

                amount.append(
                    {
                        'amount': format(aux_calcule, '.2f'),
                        'gross_ir': format(income_ir, '.2f'),
                        'income_gross': format(income_gross, '.2f'),
                        'date': date_id.strftime('%d/%m/%Y'),
                    }
                )

            income = amount[-1]

            return {
                'name': self.name,
                'amount': self.invest,
                'result_timeline': amount,
                'deadline': self.deadline,
                'finish_period': income,
                'percent_cdi': PERCENT_CDI,
                'percent_irr': PERCENT_IRR,
                'percent_rate': PERCENT_RATE
            }
        except Exception as err:
            raise err
