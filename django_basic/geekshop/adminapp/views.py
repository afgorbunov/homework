from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from setuptools.command.setopt import edit_config

from adminapp.forms import ShopUserAdminEditForm
from authapp.forms import ShopUserCreationForm
from authapp.models import ShopUser
from mainapp.models import Good, GoodsCategory


@user_passes_test(lambda u: u.is_superuser)
def home(req):
    return render(req, 'adminapp/home.html', dict())


# ====================== USERS ======================

@user_passes_test(lambda u: u.is_superuser)
def user_create(req):
    if req.method == 'POST':
        user_form = ShopUserCreationForm(req.POST, req.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('adminapp:users'))
    else:
        user_form = ShopUserCreationForm()
    return render(req, 'adminapp/user_update.html', {'update_form': user_form, })


@user_passes_test(lambda u: u.is_superuser)
def user_read(req):
    users_list = ShopUser.objects.all().order_by(
        '-is_active', '-is_superuser', '-is_staff', 'username')
    return render(req, 'adminapp/users.html', {'objects': users_list})


@user_passes_test(lambda u: u.is_superuser)
def user_update(req, pk):
    edit_user = get_object_or_404(ShopUser, pk=pk)
    if req.method == 'POST':
        edit_form = ShopUserAdminEditForm(
            req.POST, req.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('adminapp:user_update', args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)
    return render(req, 'adminapp/user_update.html', {'update_form': edit_form})


@user_passes_test(lambda u: u.is_superuser)
def user_delete(req, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    if req.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('adminapp:users'))
    return render(req, 'adminapp/user_delete.html', {'user_to_delete': user})

# ====================== CATEGORIES ======================


@user_passes_test(lambda u: u.is_superuser)
def categories(req):
    categories_list = GoodsCategory.objects.all()
    return render(req, 'adminapp/categories.html', {'objects': categories_list})


@user_passes_test(lambda u: u.is_superuser)
def category_create(req):
    pass


@user_passes_test(lambda u: u.is_superuser)
def category_update(req, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def category_delete(req, pk):
    pass

# ====================== GOODS ======================


@user_passes_test(lambda u: u.is_superuser)
def goods(req, pk):
    category = get_object_or_404(GoodsCategory, pk=pk)
    goods_list = Good.objects.filter(category__pk=pk).order_by('caption')
    return render(req, 'adminapp/goods.html', {
        'category': category,
        'goods': goods_list,
    })


@user_passes_test(lambda u: u.is_superuser)
def good_create(req):
    pass


@user_passes_test(lambda u: u.is_superuser)
def good_read(req, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def good_update(req, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def good_delete(req, pk):
    pass
