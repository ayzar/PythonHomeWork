from django.urls import path
from .views import home, shop, cart

urlpatterns = [
    path('', home, name='home'),          # Главная страница
    path('shop/', shop, name='shop'),      # Страница магазина
    path('cart/', cart, name='cart'),      # Страница корзины
]
