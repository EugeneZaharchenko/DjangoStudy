from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('create_collection/', views.create_collection),
    path('update_collection/', views.update_collection),
    path('queries/', views.get_products),
    path('order_items/', views.get_order_items),
    path('aggrs/', views.get_aggregations),
]