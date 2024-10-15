from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_up_by_html, name='html_sign_up'),  # Страница с простой HTML-формой
    path('django_sign_up/', views.sign_up_by_django, name='django_sign_up'),  # Страница с формой Django
]