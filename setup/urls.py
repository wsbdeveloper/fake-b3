from django.contrib import admin
from django.urls import path, include

from transactions.views import TransactionsViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('transaction', TransactionsViewSet, basename='Transactions')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
