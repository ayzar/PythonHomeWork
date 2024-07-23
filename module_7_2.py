def custom_write(file_name, strings):
  # Создаем пустой словарь для хранения результатов
    strings_positions = {}

  # Открываем файл для записи в текстовом режиме
    file = open(file_name, 'w', encoding='utf-8') 
    for line_number, string in enumerate(strings, start=1):
        byte_position = file.tell() + 1  # на 1 больше, т.к. будет добавлен символ \n
        file.write(string + '\n')
        strings_positions[(line_number, byte_position)] = string
  # Возвращаем полученный словарь
    return strings_positions

# Пример использования функции
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
