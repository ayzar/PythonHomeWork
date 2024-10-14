from django.shortcuts import render
from .forms import UserRegister

# Псевдо-список пользователей
users = ['existing_user1', 'existing_user2', 'existing_user3']

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
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                users.append(username)
                info['message'] = f'Приветствуем, {username}!'
        else:
            info['error'] = 'Неверно заполнена форма'

        info['form'] = form
    else:
        form = UserRegister()
        info['form'] = form

    return render(request, 'fifth_task/registration_page.html', info)


# Обработка регистрации через простую HTML форму
def sign_up_by_html(request):
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if not all([username, password, repeat_password, age]):
            info['error'] = 'Все поля должны быть заполнены'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            users.append(username)
            info['message'] = f'Приветствуем, {username}!'

    return render(request, 'fifth_task/registration_page.html', info)
