from django.urls import path
from task5 import views

urlpatterns = [
    path('', views.sign_up_by_html, name='home'),  # Страница с формой регистрации
    path('django_sign_up/', views.sign_up_by_django, name='django_sign_up'),
]
