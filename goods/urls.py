from django.urls import path
from . import views

app_name = 'goods'

urlpatterns = [
    path('search/', views.catalog, name="search"),
    path('catalog/<slug:slug_cat>/', views.catalog, name="catalog"),
    path('product/<slug:prod_slug>/', views.product, name="product"),
]