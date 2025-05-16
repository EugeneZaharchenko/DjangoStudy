from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'price', 'inventory_status', 'collection_title')
    list_editable = ('price', 'slug')
    list_select_related = ['collection']
    list_per_page = 20

    def collection_title(self, obj):
        return obj.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, obj):
        if obj.inventory <= 30:
            return 'Low'
        return 'OK'


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'membership')
    list_editable = ("membership",)
    ordering = ["first_name", "last_name"]
    list_per_page = 10


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'placed_at', 'customer')


admin.site.register(models.Collection)
admin.site.register(models.Customer, CustomerAdmin)
# admin.site.register(models.Product, ProductAdmin) use this or @admin.register
