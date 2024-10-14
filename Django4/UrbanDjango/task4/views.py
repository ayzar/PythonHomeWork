from django.shortcuts import render

def shop(request):
    # Создаем словарь с семенами
    seeds = {
        'семена': ["Томаты", "Огурцы", "Перцы", "Розы", "Тюльпаны", "Лилии"]
    }
    return render(request, 'fourth_task/shop.html', seeds)  # Передаем только один словарь

def cart(request):
    return render(request, 'fourth_task/cart.html')
from django.shortcuts import render

def home(request):
    return render(request, 'fourth_task/home.html')
