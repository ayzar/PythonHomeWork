import time
import os
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time

def linear_read(filenames):
    for filename in filenames:
        read_info(filename)

def multiprocess_read(filenames):
    with Pool() as pool:
        pool.map(read_info, filenames)

if __name__ == '__main__':
    # Определяем путь к директории, в которой находится исполняемый скрипт
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Список названий файлов, с путём относительно скрипта
    filenames = [os.path.join(script_dir, f'file{number}.txt') for number in range(1, 5)]

    # Линейный вызов
    linear_time = measure_time(linear_read, filenames)
    print(f"Время выполнения (линейный подход): {linear_time:.6f} секунд")

    # Многопроцессный вызов
    multi_time = measure_time(multiprocess_read, filenames)
    print(f"Время выполнения (многопроцессный подход): {multi_time:.6f} секунд")
