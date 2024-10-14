from django.shortcuts import render
from .forms import UserRegister

# Список пользователей (псевдо-список)
users = ['existing_user1', 'existing_user2', 'existing_user3']


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
            # Проверка возраста
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            # Проверка существования пользователя
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                # Успешная регистрация
                users.append(username)
                info['message'] = f'Приветствуем, {username}!'
        else:
            info['error'] = 'Неверно заполнена форма'

        info['form'] = form

    else:
        # Если метод GET, отображаем пустую форму
        form = UserRegister()
        info['form'] = form

    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_html(request):
    info = {}

    if request.method == 'POST':
        # Получение данных из формы
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        # Проверка паролей
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        # Проверка возраста
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        # Проверка существования пользователя
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            # Успешная регистрация
            users.append(username)
            info['message'] = f'Приветствуем, {username}!'

    return render(request, 'fifth_task/registration_page.html', info)
