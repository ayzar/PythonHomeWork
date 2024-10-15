from django.shortcuts import render
from .forms import UserRegister
from django.contrib.auth.models import User  # Импортируем модель User
from .models import Game  # Импортируем модель Game
from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer  # Импортируем модель Buyer

# Обработка регистрации через Django Forms
def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Проверка паролей
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif Buyer.objects.filter(name=username).exists():  # Проверка существования пользователя в базе
                info['error'] = 'Покупатель с таким именем уже существует'
            else:
                # Добавляем нового покупателя в базу данных
                Buyer.objects.create(name=username, age=age, balance=0)  # Создаем нового покупателя
                info['message'] = f'Приветствуем, {username}!'
        else:
            info['error'] = 'Неверно заполнена форма'

        info['form'] = form
    else:
        form = UserRegister()
        info['form'] = form

    return render(request, 'task1/registration_page.html', info)


# Представление для страницы магазина
from django.shortcuts import render
from .models import Game  # Импортируем модель Game

def shop(request):
    games = Game.objects.all()  # Получаем все игры из базы данных
    return render(request, 'task1/shop.html', {'games': games})  # Передаем коллекцию игр

# Представление для страницы корзины
def cart(request):
    return render(request, 'task1/cart.html')

# Представление для главной страницы
def home(request):
    return render(request, 'task1/home.html')
