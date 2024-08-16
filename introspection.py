from pprint import pprint
def introspection_info(obj):
  # Получаем тип объекта
  obj_type = type(obj)

  # Получаем все атрибуты и методы объекта
  attributes = dir(obj)

  # Отфильтруем методы от атрибутов
  methods = [attr for attr in attributes if callable(getattr(obj, attr))]
  non_methods = [attr for attr in attributes if not callable(getattr(obj, attr))]

  # Определяем модуль, к которому принадлежит объект
  module = obj.__class__.__module__ if hasattr(obj, '__class__') else None

  # Создаем словарь с информацией
  info = {
      'type': obj_type.__name__,
      'attributes': non_methods,
      'methods': methods,
      'module': module
  }

  return info

# Пример использования
number_info = introspection_info(42)
pprint(number_info)

# Создаем свой класс для тестирования
class MyClass:
    def __init__(self):
        self.name = "MyClass Instance"
        self.value = 42

    def my_method(self):
        return "Hello from MyClass!"

# Интроспекция объекта
my_obj = MyClass()
obj_info = introspection_info(my_obj)
pprint(obj_info)
