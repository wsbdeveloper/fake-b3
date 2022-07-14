from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from simulations.use_cases.ipca_default import IpcaDefault
from simulations.use_cases.cdi_default import CdiDefault
from simulations.models import Simulations
from simulations.serializer import (
    SimulationsSerializer,
    SimulationsSerializerTimeLine,
)


class SimulationsViewSetIpca(viewsets.ModelViewSet):
    """All simulations the database"""
    queryset = Simulations.objects.all()
    serializer_class = SimulationsSerializer

    def create(self, request):
        data = request.data

        queryset = IpcaDefault(name=data['name'],invest=data['amount'], deadline=data['deadline']).exec()
        serializer_class = SimulationsSerializerTimeLine(queryset)

        return Response(serializer_class.data)

class SimulationsViewSetCdi(viewsets.ModelViewSet):
    """All simulations the database"""
    queryset = Simulations.objects.all()
    serializer_class = SimulationsSerializer

    def create(self, request):
        data = request.data

        queryset = CdiDefault(name=data['name'],invest=data['amount'], deadline=data['deadline']).exec()
        serializer_class = SimulationsSerializerTimeLine(queryset)

        return Response(serializer_class.data)
