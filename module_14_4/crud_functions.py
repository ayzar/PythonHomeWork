import sqlite3

# Инициализация базы данных
def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT,
                        price INTEGER NOT NULL,
                        image_url TEXT)''')

    conn.commit()
    conn.close()

# Добавление продукта
def add_product(title, description, price, image_url):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Products (title, description, price, image_url) VALUES (?, ?, ?, ?)",
                   (title, description, price, image_url))

    conn.commit()
    conn.close()

# Получение всех продуктов
def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    conn.close()
    return products

# Обновление продукта
def update_product(product_id, title=None, description=None, price=None, image_url=None):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    if title:
        cursor.execute("UPDATE Products SET title = ? WHERE id = ?", (title, product_id))
    if description:
        cursor.execute("UPDATE Products SET description = ? WHERE id = ?", (description, product_id))
    if price:
        cursor.execute("UPDATE Products SET price = ? WHERE id = ?", (price, product_id))
    if image_url:
        cursor.execute("UPDATE Products SET image_url = ? WHERE id = ?", (image_url, product_id))

    conn.commit()
    conn.close()

# Удаление продукта
def delete_product(product_id):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Products WHERE id = ?", (product_id,))

    conn.commit()
    conn.close()

# Создание продуктов
def create_products():
    add_product("Vitamin Complex", "Витаминный комплекс для здоровья", 1500, "http://valayzts.beget.tech/pic/vitamin-complex-package.jpg")
    add_product("vitamin & Mineral complex", "Витаминно-Минеральный комплекс", 250, "http://valayzts.beget.tech/pic/vitamin-complex-container.jpg")
    add_product("Energy Drink", "Энергетический напиток", 300, "http://valayzts.beget.tech/pic/realistic-vitamin-complex-package2.jpg")
    add_product("Omega-3 Capsules", "Капсулы Омега-3 для сердца", 600, "http://valayzts.beget.tech/pic/realistic-vitamin-complex-package.jpg")
