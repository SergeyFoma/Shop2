from django.urls import path 
from . import views

app_name = "carts"

urlpatterns = [
    path('carts-add/<int:product_id>/', views.carts_add, name='carts_add'),
    path('carts-change/<int:product_id>/', views.carts_change, name = 'carts_change'),
    path('carts-remove/<int:product_id>/', views.carts_remove, name="carts_remove"),
]