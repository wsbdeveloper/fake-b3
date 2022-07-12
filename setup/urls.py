from django.contrib import admin
from django.urls import path, include

from simulations.views import SimulationsViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('simulation', SimulationsViewSet, basename='Simulations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
