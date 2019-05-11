from django.urls import path

from authapp import views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'), 
    path('logout/', authapp.logout, name='logout'), 
    path('user/<slug:username>', authapp.userinfo, name='userinfo'), 
    path('user/register/', authapp.reg, name='reg'), 
    path('user/edit/<slug:username>', authapp.useredit, name='useredit'), 
#    path('user/')
]
