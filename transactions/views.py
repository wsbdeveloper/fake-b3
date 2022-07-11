from black import err
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from transactions.use_cases.ipca_default import IpcaDefault
from transactions.models import Transactions
from transactions.serializer import (
    TransactionSerializer,
    TransactionSerializerTimeLine,
)


class TransactionsViewSet(viewsets.ModelViewSet):
    """All transactions the database"""
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request):
        queryset = IpcaDefault(name="transacao pix",invest=20000, deadline=200).exec()
        serializer_class = TransactionSerializerTimeLine(queryset)

        return Response(serializer_class.data)
