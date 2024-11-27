from django.shortcuts import render
from goods.models import Products
from django.core.paginator import Paginator

def catalog(request,category_slug):
	if category_slug=='vse-tovary':
		goods=Products.objects.all()
	else:
		goods=(Products.objects.filter(category__slug=category_slug))

	paginator = Paginator(goods, 3)
	#current_page = paginator.page(1)
	page_number=request.GET.get("page")
	page_obj=paginator.get_page(page_number)

	context={
		'goods':goods,
		'slug_url':category_slug,
		'page_obj':page_obj,
	}
	return render(request, 'goods/catalog.html', context=context)

def products(request, product_slug):
	prod=Products.objects.get(slug=product_slug)
	context={
		'prod':prod,
	}
	return render(request, 'goods/products.html', context=context)
