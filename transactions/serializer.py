from unittest import result
from rest_framework import serializers
from transactions.models import Transactions


class ResultTimeLine(serializers.Serializer):
    amount = serializers.CharField()
    gross_ir = serializers.CharField()
    income_gross = serializers.CharField()
    date = serializers.CharField()

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ('name', 'amount', 'result_timeline')

    result_timeline = ResultTimeLine(many=True)
