from basketapp.models import Basket
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from mainapp.models import Good


def basket(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {
        'basket': basket,
    }
    return render(request, "basketapp/basket.html", context)


def basket_add(request, pk):
    good = get_object_or_404(Good, pk=pk)
    basket = Basket.objects.filter(user=request.user, good=good).first()
    if not basket:
        basket = Basket(user=request.user, good=good)
    basket.quantity += 1
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    context = dict()
    return render(request, 'basketapp/basket.html', context)
