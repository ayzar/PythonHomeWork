from django.shortcuts import render

def home(request):
    return render(request, 'third_task/home.html')

'''
def shop(request):
    items = {
        'item1': 'Товар 1',
        'item2': 'Товар 2',
        'item3': 'Товар 3',
    }
    return render(request, 'third_task/shop.html', {'items': items})
'''
def cart(request):
    return render(request, 'third_task/cart.html')
from django.shortcuts import render

def shop(request):
    seeds = {
        'Овощи': [
            {'name': 'Помидоры', 'price': '50 руб.', 'description': 'Сладкие и сочные помидоры.'},
            {'name': 'Огурцы', 'price': '40 руб.', 'description': 'Хрустящие и свежие огурцы.'},
            {'name': 'Перец', 'price': '60 руб.', 'description': 'Яркие и вкусные перцы.'},
        ],
        'Цветы': [
            {'name': 'Розы', 'price': '100 руб.', 'description': 'Красивые и ароматные розы.'},
            {'name': 'Тюльпаны', 'price': '80 руб.', 'description': 'Яркие тюльпаны для весеннего настроения.'},
            {'name': 'Лаванда', 'price': '70 руб.', 'description': 'Ароматная лаванда для сада.'},
        ]
    }
    return render(request, 'third_task/shop.html', {'seeds': seeds})

