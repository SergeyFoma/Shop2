from django.shortcuts import render
from django.shortcuts import get_object_or_404
from goods.models import Categories, Products
from django.core.paginator import Paginator

def catalog(request, slug_cat=None):
    page = request.GET.get("page",1)
    categ = Categories.objects.get(slug=slug_cat)
    #goods = Products.objects.filter(category = categ)
    #query = request.GET.get('q', None)

    if slug_cat == 'all':
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category = categ)
    

    order_by = request.GET.get('order_by', None)
    if order_by:
        goods = goods.order_by(order_by)

    discount = request.GET.get('discount')
    if discount:
        goods = goods.filter(discount__gt=0)

    paginator = Paginator(goods, 2)
    goods=paginator.page(int(page))


    context = {
        'categ':categ,
        #'prod_categ':prod_categ,
        'goods':goods,
        'slug_url':slug_cat,
        'paginator':paginator,
    }
    return render(request, "goods/catalog.html", context)

def product(request, prod_slug):
    prod = get_object_or_404(Products, slug=prod_slug)
    context = {
        'prod':prod,
    }
    return render(request, "goods/product.html", context)
