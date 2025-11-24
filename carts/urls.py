from django.urls import path 
from . import views

app_name = "carts"

urlpatterns = [
    path('carts_add/<slug:product_slug>/', views.carts_add, name='carts_add'),
    path('carts_change/<int:product_id>', views.carts_change, name = 'carts_change'),
    path('carts_change_plus/<int:product_id>', views.carts_change_plus, name = 'carts_change_plus'),
    path('carts_remove/<int:cart_id>/', views.carts_remove, name="carts_remove"),
]