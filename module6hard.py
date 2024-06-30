class Figure:
  sides_count = 0

  def __init__(self, color, *sides):
      self.__color = self.__validate_color(*color)
      self.filled = False
      self.__sides = self.__validate_sides(*sides)

  def __validate_color(self, r, g, b):
      if self.__is_valid_color(r, g, b):
          return [r, g, b]
      else:
          return [0, 0, 0]

  def __is_valid_color(self, r, g, b):
      return all(isinstance(val, int) and 0 <= val <= 255 for val in [r, g, b])

  def set_color(self, r, g, b):
      if self.__is_valid_color(r, g, b):
          self.__color = [r, g, b]

  def get_color(self):
      return self.__color

  def __validate_sides(self, *sides):
      if len(sides) == self.sides_count and \
          all(isinstance(side, int) and side > 0 for side in sides):
          return list(sides)
      return [1] * self.sides_count

  def __is_valid_sides(self, *sides):
      return len(sides) == self.sides_count and \
      all(isinstance(side, int) and side > 0 for side in sides)

  def set_sides(self, *sides):
      if self.__is_valid_sides(*sides):
          self.__sides = list(sides)

  def get_sides(self):
      return self.__sides

  def __len__(self):
      return sum(self.__sides)


class Circle(Figure):
  sides_count = 1

  def __init__(self, color, *sides):
      super().__init__(color, *sides)
      self.__radius = self.__calculate_radius()

  def __calculate_radius(self):
      return self.get_sides()[0] / (2 * 3.14159)

  def get_square(self):
      return 3.14159 * self.__radius ** 2


class Triangle(Figure):
  sides_count = 3

  def __init__(self, color, *sides):
      super().__init__(color, *sides)
      self.__height = self.__calculate_height()

  def __calculate_height(self):
      a, b, c = self.get_sides()
      s = (a + b + c) / 2
      return (2 / a) * (s * (s - a) * (s - b) * (s - c)) ** 0.5

  def get_square(self):
      a, b, c = self.get_sides()
      s = (a + b + c) / 2
      return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Cube(Figure):
  sides_count = 12

  def __init__(self, color, *sides):
      if len(sides) == 1:
          sides = [sides[0]] * 12
      super().__init__(color, *sides)

  def get_volume(self):
      edge = self.get_sides()[0]
      return edge ** 3


# Проверка кода
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)   # Не изменится
print(circle1.get_color())  # [55, 66, 77]
print(cube1.get_color())    # [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)            # Изменится
print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
print(circle1.get_sides())  # [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  # 15

# Проверка объёма (куба):
print(cube1.get_volume())  # 216
