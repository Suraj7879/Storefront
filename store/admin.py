from django.contrib import admin
from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status']
    list_editable = ['unit_price']
    list_per_page = 10

    @admin.display(ordering = 'inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_per_page = 10
    list_editable = ['membership']
    search_fields = ['first_name__istartswith', 'last_name__startswith']

admin.site.register(models.Collection)
# admin.site.register(models.Customer)
# admin.site.register(models.Product, ProductAdmin)


