from django.urls import include, path
from adminapp import views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.home, name='home'),

    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/read/', adminapp.user_read, name='users'),
    path("users/update/<int:pk>/", adminapp.user_update, name="user_update"),
    path("users/delete/<int:pk>/", adminapp.user_delete, name="user_delete"),

    path('categories/create/', adminapp.category_create, name='category_create'),
    path('categories/read/', adminapp.categories, name='categories'),
    path('categories/update/<int:pk>/',
         adminapp.category_update, name='category_update'),
    path('categories/delete/<int:pk>/',
         adminapp.category_delete, name='category_delete'),

    path('goods/create/', adminapp.good_create, name='good_create'),
    path('goods/read/category/<int:pk>/', adminapp.goods, name='goods'),
    path('goods/read/<int:pk>/', adminapp.good_read, name='good_read'),
    path('goods/update/<int:pk>/', adminapp.good_update, name='good_update'),
    path('goods/delete/<int:pk>/', adminapp.good_delete, name='good_delete'),
]
