from django.urls import path
from . import views

urlpatterns = [
    path('create-flower/', views.create_flower, name='create_flower'),
    path('create-client/', views.create_client, name='create_client'),
    path('get_flower/', views.get_flower, name='get_flower'),
    path('try_form/', views.my_form, name='my_form'),
    path('try_form_class/', views.MyFormView.as_view(), name='my_form'),
    path('try_form_model/', views.ModelFormView.as_view(), name='my_form'),
]
