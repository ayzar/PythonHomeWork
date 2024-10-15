from django.urls import path
from . import views
from django.urls import path
from .views import sign_up_by_django, shop, cart, home  # Импортируем представления

urlpatterns = [
    path('sign-up/', sign_up_by_django, name='sign_up'),  # Страница регистрации
    path('shop/', shop, name='shop'),                     # Страница магазина
    path('cart/', cart, name='cart'),                     # Страница корзины
    path('', home, name='home'),                          # Главная страница
]
