from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task2/', include('task2.urls')),  # Подключение маршрутов приложения task2
    path('task3/', include('task3.urls')),  # Подключаем маршруты приложения task3
    path('task4/', include('task4.urls')),  # Подключаем маршруты приложения task4
    path('task5/', include('task5.urls')),

    path('', RedirectView.as_view(url='/task5/', permanent=True)),  # Перенаправляем с корневого URL на task5
]


