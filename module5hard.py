import hashlib
import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password):
    # Метод для хэширования пароля
      return int(hashlib.sha256(password.encode()).hexdigest(), 16)

    def check_password(self, password):
    # Метод для проверки пароля
      return self.password == int(hashlib.sha256(password.encode()).hexdigest(), 16)

    def __str__(self):
              return f"User(nickname={self.nickname}, \
      password={self.password}, \
      age={self.age})"

class Video:
  def __init__(self, title, duration, time_now=0, adult_mode=False):
      self.title = title  
      self.duration = duration  
      self.time_now = time_now  
      self.adult_mode = adult_mode

class UrTube:
  def __init__(self):
      self.users = []
      self.videos = []
      self.current_user = None

  def register(self, nickname, password, age):
    for user in self.users:
        if user.nickname == nickname:
            print(f"Пользователь {nickname} уже существует")
            return
    new_user = User(nickname, password, age)
    self.users.append(new_user)
    self.current_user = new_user
    print(f"Пользователь {nickname} успешно зарегистрирован")

  def log_in(self, login, password):
    for user in self.users:
        if user.nickname == login and user.check_password(password):
            self.current_user = user
            return
    print("Неверный логин или пароль")

  def log_out(self):
    self.current_user = None  

  def add(self, *new_videos):
    for video in new_videos:
        if all(v.title != video.title for v in self.videos):
            self.videos.append(video)
            print(f"Видео {video.title} успешно добавлено")  

  def get_videos(self, keyword):
    keyword_lower = keyword.lower()
    return [video.title for video in self.videos if keyword_lower in video.title.lower()]  

  def watch_video(self, title):
    if self.current_user is None:
        print("Войдите в аккаунт, чтобы смотреть видео")
        return
    for video in self.videos:
        if video.title == title:
            if video.adult_mode and self.current_user.age < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
                return
            for second in range(video.time_now, video.duration):
                print(f"Секунда: {second + 1}")
                time.sleep(1)
            video.time_now = 0
            print("Конец видео")
            return
    print("Видео не найдено")

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')