# Глобальная переменная для подсчёта вызовов
calls = 0

# Функция для увеличения счётчика вызовов
def count_calls():
    global calls
    calls += 1

# Функция string_info: принимает строку и возвращает кортеж
def string_info(string):
    count_calls()  # Увеличиваем счётчик вызовов
    return len(string), string.upper(), string.lower()

# Функция is_contains: проверяет наличие строки в списке (без учёта регистра)
def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счётчик вызовов
    string_lower = string.lower()  # Приводим строку к нижнему регистру
    list_lower = [item.lower() for item in list_to_search]  # Приводим все элементы списка к нижнему регистру
    return string_lower in list_lower

# Примеры вызовов функций
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

# Выводим количество вызовов
print(calls)