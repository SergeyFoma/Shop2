from django.shortcuts import redirect, render

from goods.models import Products
from carts.models import Cart

def carts_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user = request.user, product=product)
        
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user = request.user, product=product, quantity = 1)
    return redirect(request.META['HTTP_REFERER'])

def carts_change(request, product_id=None):
    
    cart_user = Cart.objects.get(id=product_id)
    print(cart_user.quantity)
    if request.user.is_authenticated:
        if cart_user.quantity > 0:
            cart_user.quantity -= 1
            print('res==', cart_user)
            cart_user.save()
    
    return redirect(request.META['HTTP_REFERER'])
    #return render(request, "carts/carts_change.html", context)

def carts_change_plus(request, product_id=None):
    
    cart_user = Cart.objects.get(id=product_id)
    print(cart_user.quantity)
    if request.user.is_authenticated:
        if cart_user.quantity >= 0:
            cart_user.quantity += 1
            print('res==', cart_user)
            cart_user.save()
    
    return redirect(request.META['HTTP_REFERER'])



def carts_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])
