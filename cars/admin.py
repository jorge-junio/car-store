from django.contrib import admin
from cars.models import Car, Brand


class BrandAdmin(admin.ModelAdmin):
    # são os campos que irão aparecer na listagem de Cars do admin
    list_display = ('name',)
    # qual o campo que permite a filtragem no admin
    search_fields = ('name',)


class CarAdmin(admin.ModelAdmin):
    # são os campos que irão aparecer na listagem de Cars do admin
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    # qual o campo que permite a filtragem no admin
    search_fields = ('model', 'brand')


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
