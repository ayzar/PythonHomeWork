from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from task1.views import sign_up_by_django, home, cart, shop

urlpatterns = [
    path('admin/', admin.site.urls),                  # Админ-панель
    path('sign-up/', sign_up_by_django, name='django_sign_up'),  # Страница регистрации
    path('', home, name='home'),                      # Главная страница
    path('shop/', shop, name='shop'),                 # Страница магазина
    path('cart/', cart, name='cart'),                 # Страница корзины
    path('task1/', include('task1.urls')),  # Подключение маршрутов приложения task1
]