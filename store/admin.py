from django.contrib import admin
from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price']
    list_editable = ['unit_price']
    list_per_page = 10

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_per_page = 10
    list_editable = ['membership']

admin.site.register(models.Collection)
# admin.site.register(models.Customer)
# admin.site.register(models.Product, ProductAdmin)


