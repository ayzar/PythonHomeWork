from django.urls import path
from .views import class_view, function_view

urlpatterns = [
    path('class/', class_view, name='class_view'),
    path('func/', function_view, name='function_view'),
]
