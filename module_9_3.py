first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для вычисления разницы длин строк, если их длины не равны
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

# Генераторная сборка для сравнения длин строк на одинаковых позициях без zip
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Преобразование генераторов в списки и вывод результатов
print(list(first_result))  # Вывод: [1, 2]
print(list(second_result))  # Вывод: [False, False, True]