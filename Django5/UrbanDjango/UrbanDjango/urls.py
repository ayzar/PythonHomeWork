from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task2/', include('task2.urls')),
    path('task3/', include('task3.urls')),
    path('task4/', include('task4.urls')),
    path('task5/', include('task5.urls')),

    # Редирект с корневого URL на страницу task5
    path('', RedirectView.as_view(url='/task5/', permanent=True)),
]
