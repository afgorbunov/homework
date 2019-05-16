from basketapp import views as basketapp
from django.urls import path

app_name = 'basketapp'

urlpatterns = [
    path("", basketapp.basket, name="view"),
    path('add/<int:pk>/', basketapp.basket_add, name='add'),
    path('remove/<int:pk>/', basketapp.basket_remove, name='remove'),
]