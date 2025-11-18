from django.urls import path 
from . import views

app_name = "carts"

urlpatterns = [
    path('carts_add/<slug:product_slug>/', views.carts_add, name='carts_add'),
    path('carts_change/<slug:product_slug>/', views.carts_change, name = 'carts_change'),
    path('carts_remove/<slug:product_slug>/', views.carts_remove, name="carts_remove"),
]