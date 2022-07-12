import os
from datetime import date
from dateutil.relativedelta import relativedelta
from decimal import Decimal
from pyparsing import Char

PERCENT_IPCA = os.getenv('IPCA_DEFAULT', 6)
PERCENT_IRR = os.getenv('IPCA_IRR', 0.85)
PERCENT_RATE = os.getenv('IPCA_RATE', 6.05)

class HelpersIpca:
    def __init__(self, invest: int, name: Char, deadline: int) -> None:
        self.invest = invest
        self.name = name
        self.deadline = deadline

    @property
    def contract_fee(self):
        taxa = (PERCENT_RATE / 100) + 1
        result = (taxa) ** (1 / 12)

        return result

    @property
    def ipca(self):
        ipca_calcule = (PERCENT_IPCA / 100) + 1
        result = (ipca_calcule) ** (1 / 12)

        return result

    @property
    def summation(self):
        ipca = self.ipca
        taxa = self.contract_fee
        return (ipca + taxa) - 1

    def patrimony(self, contribution: int):
        summ = self.summation

        return contribution * summ

    def patrymony_with_taxes(self, contribution: int):
        return (self.patrimony(contribution) - contribution) * 0.85

    def patrymony_without_taxes(self, contribution: int):
        return self.patrimony(contribution) - contribution

    def exec(self):
        try:
            amount = []
            aux_calcule = 0

            date_id = date.today() + relativedelta(months=1)
            aux_calcule = self.patrimony(contribution=self.invest)
            income_ir = self.patrymony_with_taxes(contribution=self.invest)
            income_gross = self.patrymony_without_taxes(
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
                aux_calcule = self.patrimony(contribution=aux_calcule)

                # rendimento com imposto
                income_ir = self.patrymony_with_taxes(contribution=aux_calcule)

                # rendimento sem imposto
                income_gross = self.patrymony_without_taxes(
                    contribution=aux_calcule
                )

                amount.append(
                    {
                        'amount': format(aux_calcule, '.2f'),
                        'gross_ir': format(income_ir, '.2f'),
                        'income_gross': format(income_gross, '.2f'),
                        'date': date_id.strftime('%d/%m/%Y'),
                    }
                )

            income = amount[-1]

            breakpoint()
            return {
                'name': self.name,
                'amount': self.invest,
                'result_timeline': amount,
                'deadline': self.deadline,
                'finish_period': income,
                'percent_ipca': PERCENT_IPCA,
                'percent_irr': PERCENT_IRR,
                'percent_rate': PERCENT_RATE
            }
        except Exception as err:
            raise err
