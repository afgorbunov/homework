from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.template.loader import render_to_string
from django.urls import reverse

from basketapp.models import Basket
from mainapp.models import Good


@login_required
def basket(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {
        'basket': basket,
    }
    return render(request, "basketapp/basket.html", context)


@login_required
def basket_add(request, pk):
    good = get_object_or_404(Good, pk=pk)
    basket = Basket.objects.filter(user=request.user, good=good).first()
    if not basket:
        basket = Basket(user=request.user, good=good)
    basket.quantity += 1
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    good = get_object_or_404(Good, pk=pk)
    basket = Basket.objects.filter(user=request.user, good=good).first()
    if basket:
        basket.quantity -= 1
        basket.save()
        if basket.quantity == 0:
            basket.delete()
    return HttpResponseRedirect(reverse('basket:view'))


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_basket_item = Basket.objects.get(pk=int(pk))
        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()
        basket_items = Basket.objects.filter(
            user=request.user).order_by('good__category')
        context = {
            'basket_items': basket_items,
        }
        result = render_to_string(
            'basketapp/includes/inc_basket_list.html', context)
        return JsonResponse({'result': result})
