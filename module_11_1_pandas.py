import pandas as pd


# 1. Создание и просмотр DataFrame
data = {
    'Name': ['Алиса', 'Никита', 'Рашид'],
    'Age': [25, 30, 35],
    'City': ['Москва', 'Санкт-Петербург', 'Казань']
}
df = pd.DataFrame(data, index=[1, 2, 3])
print("Созданный DataFrame с индексами, начинающимися с 1:")
print(df)

# 2. Чтение и запись данных
df.to_csv('people.csv', index=True)  # Сохраняем DataFrame в CSV файл с индексами

# Читаем данные из CSV файла
df_loaded = pd.read_csv('people.csv', index_col=0)  # Устанавливаем первый столбец как индекс
print("\nЗагруженные данные из CSV с индексами:")
print(df_loaded)

# 3. Основные операции с данными
# Фильтрация данных (возраст больше 30)
filtered_df = df[df['Age'] > 30]
print("\nОтфильтрованные данные (возраст больше 30):")
print(filtered_df)

# Вычисление статистики (средний возраст)
mean_age = df['Age'].mean()
print(f"\nСредний возраст: {mean_age}")

# Работа с пропущенными значениями
df_with_nan = df.copy()
df_with_nan.loc[2, 'City'] = None  # Устанавливаем пропущенное значение
df_filled = df_with_nan.fillna('Unknown')  # Заполняем пропущенные значения
print("\nDataFrame с заполненными пропущенными значениями:")
print(df_filled)

# 4. Группировка и агрегирование
# Группировка по городам и подсчёт количества людей в каждом городе
grouped_df = df.groupby('City').size()
print("\nКоличество людей в каждом городе:")
print(grouped_df)import pandas as pd

# 1. Создание и просмотр DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print("Созданный DataFrame:")
print(df)

# 2. Чтение и запись данных
# Сохраняем DataFrame в CSV файл
df.to_csv('people.csv', index=False)

# Читаем данные из CSV файла
df_loaded = pd.read_csv('people.csv')
print("\nЗагруженные данные из CSV:")
print(df_loaded)

# 3. Основные операции с данными
# Фильтрация данных (возраст больше 30)
filtered_df = df[df['Age'] > 30]
print("\nОтфильтрованные данные (возраст больше 30):")
print(filtered_df)

# Вычисление статистики (средний возраст)
mean_age = df['Age'].mean()
print(f"\nСредний возраст: {mean_age}")

# Работа с пропущенными значениями
df_with_nan = df.copy()
df_with_nan.loc[1, 'City'] = None  # Устанавливаем пропущенное значение
df_filled = df_with_nan.fillna('Unknown')  # Заполняем пропущенные значения
print("\nDataFrame с заполненными пропущенными значениями:")
print(df_filled)

# 4. Группировка и агрегирование
# Группировка по городам и подсчёт количества людей в каждом городе
grouped_df = df.groupby('City').size()
print("\nКоличество людей в каждом городе:")
print(grouped_df)
