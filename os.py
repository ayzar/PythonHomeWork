
import os
import time

# Укажите путь к каталогу, который хотите обойти
directory = "."

# Обход каталога
for root, dirs, files in os.walk(directory):
    for file in files:
        # Формирование полного пути к файлу
        filepath = os.path.join(root, file)

        # Получение времени последнего изменения
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Получение размера файла
        filesize = os.path.getsize(filepath)

        # Получение родительской директории
        parent_dir = os.path.dirname(filepath)

        # Вывод информации о файле
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} /байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
