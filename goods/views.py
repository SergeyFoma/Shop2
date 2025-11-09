from django.shortcuts import render
from django.shortcuts import get_object_or_404
from goods.models import Categories

def catalog(request, slug_cat):
    categ = Categories.objects.get(slug=slug_cat)
    context = {
        'categ':categ,
    }
    return render(request, "goods/catalog.html", context)

def product(request):
    context = {

    }
    return render(request, "goods/product.html", context)
