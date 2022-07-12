from unittest import result

from rest_framework import serializers

from simulations.models import Simulations


class ResultTimeLine(serializers.Serializer):
    amount = serializers.CharField()
    gross_ir = serializers.CharField()
    income_gross = serializers.CharField()
    date = serializers.CharField()


class SimulationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Simulations
        fields = ('name', 'amount')


class SimulationsSerializerTimeLine(serializers.ModelSerializer):
    class Meta:
        model = Simulations
        fields = ('name', 'amount', 'result_timeline', 'percent_ipca','percent_irr', 'percent_rate','deadline')

    deadline = serializers.IntegerField()
    percent_ipca = serializers.DecimalField(max_digits=10, decimal_places=2)
    percent_irr = serializers.DecimalField(max_digits=10, decimal_places=2)
    percent_rate = serializers.DecimalField(max_digits=10, decimal_places=2)
    result_timeline = ResultTimeLine(many=True)
