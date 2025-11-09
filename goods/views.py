from django.shortcuts import render
from django.shortcuts import get_object_or_404
from goods.models import Categories, Products

def catalog(request, slug_cat):
    categ = Categories.objects.get(slug=slug_cat)
    goods = Products.objects.filter(category = categ)

    if slug_cat == 'all':
        goods = Products.objects.all()
    context = {
        'categ':categ,
        #'prod_categ':prod_categ,
        'goods':goods,
    }
    return render(request, "goods/catalog.html", context)

def product(request, prod_slug):
    prod = get_object_or_404(Products, slug=prod_slug)
    context = {
        'prod':prod,
    }
    return render(request, "goods/product.html", context)
