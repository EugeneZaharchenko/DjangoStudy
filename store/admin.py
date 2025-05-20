from django.contrib import admin
from django.http import HttpRequest
from django.db.models import QuerySet, Count
from django.urls import reverse
from django.utils.html import format_html, urlencode
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


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'products_count')

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = reverse("admin:store_product_changelist") + '?' + urlencode({
            'collection__id': str(collection.id)
        })
        return format_html('<a href="{}">{}</a>', url, collection.products_count)

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )

admin.site.register(models.Customer, CustomerAdmin)
# admin.site.register(models.Product, ProductAdmin) use this or @admin.register
