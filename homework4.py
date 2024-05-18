# Задайте переменные разных типов данных:
# - Создайте переменную immutable_var и присвойте ей кортеж из нескольких
# элементов разных типов данных.
# - Выполните операции вывода кортежа immutable_var на экран.
immutable_var = 1.5, "Строка", True, [1, 2, 3]
print("Immutable tuple: ",immutable_var)
# Изменение значений переменных:
# - Попытайтесь изменить элементы кортежа immutable_var. Объясните,
# изменить значения элементов кортежа.

# immutable_var[0] = 2
# Выдает ошибку:  TypeError: 'tuple' object does not support item assignment
# Кортеж относится к иммутабельному (неизменяемому) типу данных,
# поэтому его элементы не могут быть измены

# Создание изменяемых структур данных:
# - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
# - Измените элементы списка mutable_list.
# - Выведите на экран измененный список mutable_list.
mutable_list = [1, 2, 3]
print("Mutable list: ", mutable_list)
mutable_list[1] = 4
print("Modified mutable list: ", mutable_list)
