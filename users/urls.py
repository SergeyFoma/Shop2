from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('login_user/', views.login_user, name='login_user'),
    path('registration/', views.registration, name="registration"),
    path('profile/', views.profile, name="profile"),
    path('users-cart/', views.users_cart, name='users_cart'),
    path('logout_user/', views.logout_user, name="logout_user"),
]
