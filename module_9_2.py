first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Список из длин строк списка first_strings, если длина строки >= 5
first_result = [len(s) for s in first_strings if len(s) >= 5]

# Список пар слов одинаковой длины из first_strings и second_strings
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

# Словарь строка-длина строки для объединенных списков, если длина строки четная
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Вывод результатов
print(first_result)  # [10, 8, 8]
print(second_result)  # [('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]
print(third_result)  # {'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}
