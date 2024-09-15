import sqlite3

# Подключаемся к базе данных (если файла не существует, он будет создан)
conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

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
SET balance = 500
WHERE id % 2 = 1
''')

# Удаляем каждую 3-ю запись в таблице начиная с 1-й
cursor.execute('''
DELETE FROM Users
WHERE id % 3 = 0
''')

# Делаем выборку всех записей, где возраст не равен 60
cursor.execute('''
SELECT username, email, age, balance
FROM Users
WHERE age != 60
''')

# Получаем все результаты выборки
rows = cursor.fetchall()

# Выводим результаты в консоль
for row in rows:
    print(f'Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}')

# Сохраняем изменения и закрываем соединение с базой данных
conn.commit()
conn.close()