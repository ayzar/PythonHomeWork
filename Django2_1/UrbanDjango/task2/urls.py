from django.urls import path
from .views import func_view, ClassView

urlpatterns = [
    path('func/', func_view, name='func_view'),
    path('class/', ClassView.as_view(), name='class_view'),
]
