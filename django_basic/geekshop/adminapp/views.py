from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from setuptools.command.setopt import edit_config

from adminapp.forms import ShopUserAdminEditForm
from authapp.forms import ShopUserCreationForm
from authapp.models import ShopUser
from mainapp.models import Good, GoodsCategory


@user_passes_test(lambda u: u.is_superuser)
def home(req):
    return render(req, 'adminapp/home.html', dict())


# ====================== USERS ======================


class ShopUserCreateView(CreateView):
    model = ShopUser
    template_name = "adminapp/user_update.html"
    fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ShopUserList(ListView):
    model = ShopUser
    context_object_name = ''
    template_name = 'adminapp/users.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ShopUserUpdateView(UpdateView):
    model = ShopUser
    template_name = "adminapp/user_update.html"
    fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ShopUserDeleteView(DeleteView):
    model = ShopUser
    template_name = "adminapp/user_delete.html"
    success_url = reverse_lazy('adminapp:users')

    def delete(self, req, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# ====================== CATEGORIES ======================


class GoodsCategoryListView(ListView):
    model = GoodsCategory
    template_name = "adminapp/categories.html"

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class GoodsCategoryCreateView(CreateView):
    model = GoodsCategory
    template_name = "adminapp/category_update.html"
    success_url = reverse_lazy('adminapp:categories')
    fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class GoodsCategoryUpdateView(UpdateView):
    model = GoodsCategory
    template_name = "adminapp/category_update.html"
    success_url = reverse_lazy('adminapp:categories')
    fields = '__all__'

    def get_cotext_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории / редактирование'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class GoodsCategoryDeleteView(DeleteView):
    model = GoodsCategory
    template_name = "adminapp/category_delete.html"
    success_url = reverse_lazy('adminapp:categories')

    def delete(self, req, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# ====================== GOODS ======================


@user_passes_test(lambda u: u.is_superuser)
def goods(req, pk):
    category = get_object_or_404(GoodsCategory, pk=pk)
    goods_list = Good.objects.filter(category__pk=pk).order_by('caption')
    return render(req, 'adminapp/goods.html', {
        'category': category,
        'goods': goods_list,
    })


class GoodCreateView(CreateView):
    model = Good
    template_name = "adminapp/good_create.html"
    fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class GoodDetailView(DetailView):
    model = Good
    template_name = "adminapp/good_read.html"

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class GoodUpdateView(UpdateView):
    model = Good
    template_name = "adminapp/good_create.html"
    fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class GoodDeleteView(DeleteView):
    model = Good
    template_name = "adminapp/good_delete.html"
    success_url = reverse_lazy('adminapp:goods', kwargs={'pk': 1})

    def delete(self, req, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
