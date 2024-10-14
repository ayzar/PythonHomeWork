from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task2/', include('task2.urls')),  # Подключение маршрутов приложения task2
    path('task3/', include('task3.urls')),  # Подключаем маршруты приложения task3
    path('', RedirectView.as_view(url='/task3/', permanent=True)),  # Перенаправляем с корневого URL на task3
]


