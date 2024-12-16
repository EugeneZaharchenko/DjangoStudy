from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('queries/', views.get_products),
    path('order_items/', views.get_order_items),
    path('aggrs/', views.get_aggregations),
]