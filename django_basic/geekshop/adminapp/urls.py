from django.urls import include, path
from adminapp import views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.home, name='home'),

    path('users/create/', adminapp.ShopUserCreateView.as_view(), name='user_create'),
    path('users/read/', adminapp.ShopUserList.as_view(), name='users'),
    path("users/update/<int:pk>/", adminapp.ShopUserUpdateView.as_view(), name="user_update"),
    path("users/delete/<int:pk>/", adminapp.ShopUserDeleteView.as_view(), name="user_delete"),

    path('categories/create/', adminapp.GoodsCategoryCreateView.as_view(), name='category_create'),
    path('categories/read/', adminapp.GoodsCategoryListView.as_view(), name='categories'),
    path('categories/update/<int:pk>/',
         adminapp.GoodsCategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/',
         adminapp.GoodsCategoryDeleteView.as_view(), name='category_delete'),

    path('goods/create/', adminapp.GoodCreateView.as_view(), name='good_create'),
    path('goods/read/category/<int:pk>/', adminapp.goods, name='goods'),
    path('goods/read/<int:pk>/', adminapp.GoodDetailView.as_view(), name='good_read'),
    path('goods/update/<int:pk>/', adminapp.GoodUpdateView.as_view(), name='good_update'),
    path('goods/delete/<int:pk>/', adminapp.GoodDeleteView.as_view(), name='good_delete'),
]
