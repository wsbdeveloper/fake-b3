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
        fields = ('name', 'amount')


class TransactionSerializerTimeLine(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ('name', 'amount', 'result_timeline', 'percent_ipca','percent_irr', 'percent_rate')

    percent_ipca = serializers.DecimalField(max_digits=10, decimal_places=2)
    percent_irr = serializers.DecimalField(max_digits=10, decimal_places=2)
    percent_rate = serializers.DecimalField(max_digits=10, decimal_places=2)
    result_timeline = ResultTimeLine(many=True)
