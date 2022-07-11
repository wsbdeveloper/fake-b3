from django.contrib import admin

from transactions.models import Transactions as Model


class Transactions(admin.ModelAdmin):
    list_display = ('id', 'name', 'amount')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


admin.site.register(Model, Transactions)
