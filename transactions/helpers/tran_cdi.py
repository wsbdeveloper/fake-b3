import os

from datetime import date
from dateutil.relativedelta import relativedelta

class TransactionIpca:
    def __init__(self, invest: int, deadline: int) -> None:
        self.invest = invest
        self.deadline = deadline
        self.ipca = os.getenv('IPCA_DEFAULT', 6)
        self.irr = os.getenv('IPCA_IRR', 0.85)

    def contract_fee(self):
        taxa = (6.05 / 100) + 1
        result = (taxa) ** (1 / 12)

        return result

    def ipca_default(self):
        ipca_calcule = (self.ipca / 100) + 1
        result = (ipca_calcule) ** (1 / 12)

        return result

    def summation(self):
        ipca = self.ipca_default()
        taxa = self.contract_fee()
        return (ipca + taxa) - 1

    def patrimony(self, contribution: int):
        summ = self.summation()

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
            income_gross = self.patrymony_without_taxes(contribution=self.invest)

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
                income_gross = self.patrymony_without_taxes(contribution=aux_calcule)

                amount.append(
                    {
                        'amount': format(aux_calcule, '.2f'),
                        'gross_ir': format(income_ir, '.2f'),
                        'income_gross': format(income_gross, '.2f'),
                        'date': date_id.strftime('%d/%m/%Y'),
                    }
                )

            income = amount[-1]

            return {'name': 'jose', 'amount': 23.1111,'result_timeline': amount, 'finish_period': income}
        except Exception as err:
            raise err
