from django.contrib import admin
from django.urls import path, include

from simulations.views import SimulationsViewSetIpca, SimulationsViewSetCdi
from rest_framework import routers

router = routers.DefaultRouter()

router.register('simulation/ipca', SimulationsViewSetIpca, basename='SimulationsIpca')
router.register('simulation/cdi', SimulationsViewSetCdi, basename='SimulationsCdi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
