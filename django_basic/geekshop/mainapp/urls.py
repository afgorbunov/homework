from django.urls import path
from .views import catalog, item, category

app_name = 'mainapp'

urlpatterns = [
    path('', catalog, name="index"), 
    path('category/<int:category_id>', category, name="category"), 
    path('item/<int:item_id>', item, name="item"), 
]
