from django.contrib import admin

from simulations.models import Simulations as Model


class Simulations(admin.ModelAdmin):
    list_display = ('id', 'name', 'amount')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


admin.site.register(Model, Simulations)
