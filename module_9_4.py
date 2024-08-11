first = 'Мама мыла раму'
second = 'Рамена мало было'

# Используем lambda-функцию для сравнения символов на одинаковых позициях
result = list(map(lambda x, y: x == y, first, second))

print(result)

def get_advanced_writer(file_name):
  def write_everything(*data_set):
      with open(file_name, 'a', encoding='utf-8') as file:
          for item in data_set:
              file.write(f"{item}\n")
  return write_everything

# Используем замыкание для записи в файл
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
