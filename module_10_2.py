import threading
import time

class Knight(threading.Thread):
  def __init__(self, name, power):
      super().__init__()
      self.name = name
      self.power = power

  def run(self):
      enemies = 100
      days = 0
      print(f"{self.name}, на нас напали!")

      while enemies > 0:
          days += 1
          enemies -= self.power
          print(f"{self.name} сражается {days} день(дня)..., осталось {max(0, enemies)} воинов.")
          time.sleep(1)

      print(f"{self.name} одержал победу спустя {days} день(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

print("Все битвы закончились!")