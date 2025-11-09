from django.urls import path
from . import views

app_name = 'goods'

urlpatterns = [
    path('catalog/<slug:slug_cat>/', views.catalog, name="catalog"),
    path('product/', views.product, name="product"),
]