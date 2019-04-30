from django.urls import path
from .views import catalog, item

app_name = 'mainapp'

urlpatterns = [
    path('', catalog, name="index"), 
    path('<int:item_id>', item, name="item"), 
]
