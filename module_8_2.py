def personal_sum(numbers):
  result = 0
  incorrect_data = 0
  for item in numbers:
      try:
          result += float(item)  # Преобразуем элемент в число
      except (TypeError, ValueError):
          print(f'Некорректный тип данных для подсчёта суммы - {item}')
          incorrect_data += 1
  return result, incorrect_data

def calculate_average(numbers):
  if not isinstance(numbers, (list, tuple, set, str)):
      print('В numbers записан некорректный тип данных')
      return None

  try:
      if not numbers:  # Проверка на пустую коллекцию
          return 0
      result, incorrect_data = personal_sum(numbers)
      count = len(numbers) - incorrect_data
      return result / count if count > 0 else 0
  except ZeroDivisionError:
      return 0

# Пример выполнения программы:
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, каждый символ проверяется
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
print(f'Результат 5: {calculate_average([])}')