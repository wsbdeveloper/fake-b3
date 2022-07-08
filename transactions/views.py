from black import err
from rest_framework import viewsets
from transactions.app.exceptions.transactionException import TransactionExceptionServer
from transactions.models import Transactions
from transactions.serializer import TransactionSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.exceptions import APIException


class TransactionsViewSet(viewsets.ModelViewSet):
    """All transactions the database"""
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
