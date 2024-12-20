from django.urls import path
from . import views
from .views import ShowParamsView

urlpatterns = [
    path('hello/', views.hello),
    path('hi_templ/', views.hi_templ),
    path('create_collection/', views.create_collection),
    path('queries/', views.get_products),
    path('order_items/', views.get_order_items),
    path('aggrs/', views.get_aggregations),
    path('show_params/', views.show_params),
    path('show_params/<str:view>/', ShowParamsView.as_view(), name='show_params'),
    path('wrong/', views.wrong_view),
    path('static/', views.return_static),
]