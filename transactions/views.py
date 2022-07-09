from black import err
from rest_framework import viewsets
from transactions.helpers.tran_cdi import TransactionIpca
from transactions.models import Transactions
from transactions.serializer import TransactionSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from rest_framework.exceptions import APIException


class TransactionsViewSet(viewsets.ModelViewSet):
    """All transactions the database"""


    def list(self, request):
        queryset = TransactionIpca(invest=20000, deadline=200).exec()
        print(queryset)
        serializer_class = TransactionSerializer(queryset)
        return Response(serializer_class.data)

    def simulation():
        queryset = TransactionIpca().exec()
        serializer = TransactionSerializer(data=queryset)
        return Response(serializer.data)
