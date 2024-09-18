import sqlite3

# Подключаемся к базе данных (если файла не существует, он будет создан)
conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

# Удаление таблицы Users, если она существует
cursor.execute('DROP TABLE IF EXISTS Users')

# Создаем таблицу Users, если она еще не создана
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# Заполняем таблицу 10 записями
users = [
    ('User1', 'example1@gmail.com', 10, 1000),
    ('User2', 'example2@gmail.com', 20, 1000),
    ('User3', 'example3@gmail.com', 30, 1000),
    ('User4', 'example4@gmail.com', 40, 1000),
    ('User5', 'example5@gmail.com', 50, 1000),
    ('User6', 'example6@gmail.com', 60, 1000),
    ('User7', 'example7@gmail.com', 70, 1000),
    ('User8', 'example8@gmail.com', 80, 1000),
    ('User9', 'example9@gmail.com', 90, 1000),
    ('User10', 'example10@gmail.com', 100, 1000)
]

cursor.executemany('''
INSERT INTO Users (username, email, age, balance)
VALUES (?, ?, ?, ?)
''', users)

# Обновляем balance у каждой 2-й записи начиная с 1-й на 500
cursor.execute('''
UPDATE Users
SET balance = balance - 500
WHERE id % 2 == 1
''')

# Удаляем каждую 3-ю запись в таблице начиная с 1-й
cursor.execute('''
DELETE FROM Users
WHERE id % 3 == 1
''')

# Делаем выборку всех записей, где возраст не равен 60
cursor.execute('''
SELECT username, email, age, balance
FROM Users
WHERE age != 60
''')

# Получаем все результаты выборки
rows = cursor.fetchall()


# Выполняем SELECT для всех записей в таблице Users
cursor.execute('''
SELECT * FROM Users
''')

# Получаем все результаты выборки
rows = cursor.fetchall()


# Удаление записи с id = 6 (если она существует после предыдущих удалений)
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

# Удаление записи с id = 6, если она существует
cursor.execute("DELETE FROM Users WHERE id = 6") #  <-  исправлено

# Подсчитываем общее количество записей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
print(f'Общее количество пользователей: {total_users}')

# Подсчитываем сумму всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]
print(f'Сумма всех балансов: {all_balances}')



# Выводим средний баланс всех пользователей
if total_users > 0:
    average_balance = all_balances / total_users
    print(f'Средний баланс всех пользователей: {average_balance:.2f}')
else:
    print('Нет пользователей для расчета среднего баланса.')

# Вывод содержимого таблицы Users
cursor.execute("SELECT * FROM Users")
rows = cursor.fetchall()

# Красивый вывод с форматированием
print("-" * 30)  # Разделитель
print("Содержимое таблицы Users:")
print("-" * 30)
for row in rows:
    print(f"ID: {row[0]}, Username: {row[1]}, Email: {row[2]}, Age: {row[3]}, Balance: {row[4]}")  # Вывод полей
print("-" * 30)

# Сохраняем изменения и закрываем соединение с базой данных
conn.commit()
conn.close()