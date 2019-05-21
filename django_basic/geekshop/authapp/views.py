from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.urls import reverse

from authapp.forms import (ShopUserLoginForm, ShopUserCreationForm,
                           ShopUserEditForm)
from authapp.models import ShopUser

# Create your views here.


def login(request):
    title = 'вход'

    login_form = ShopUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
    content = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


@login_required
def userinfo(request, username):
    human = get_object_or_404(ShopUser, username=username)
    return render(request, 'authapp/userinfo.html', {'human': human})


def reg(request):
    title = 'регистрация'
    context = dict()
    if request.method == 'POST':
        register_form = ShopUserCreationForm(request.POST, request.FILES)
        context = {
            'title': title,
            'register_form': register_form,
        }

    return render(request, 'authapp/reg.html', context)


@login_required
def useredit(request, username):
    title = 'редактирование'
    user = get_object_or_404(ShopUser, username=username)
    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES,
                                     instance=user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:useredit', args=[username]))
    else:
        edit_form = ShopUserEditForm(instance=user)
    context = {'title': title, 'edit_form': edit_form, 'user': user}
    return render(request, 'authapp/useredit.html', context)
