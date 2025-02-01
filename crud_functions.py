import sqlite3


def initiate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')
    connection.commit()
    connection.close()  # Закрываем соединение после выполнения


def populate_db():
    connection = sqlite3.connect('products.db')  # Новое подключение
    cursor = connection.cursor()
    cursor.executescript('''
        INSERT INTO Products (title, description, price) VALUES (
            "EcoGreen Multi",
            "Мультивитамины без железа, в капсулах, 180 шт.",
            40);
        INSERT INTO Products (title, description, price) VALUES (
            "Magnesium Glycinate",
            "Пищевая добавка «Магния глицинат» 100 мг, 180 шт.",
            32);
        INSERT INTO Products (title, description, price) VALUES (
            "Omega-3",
            "Капсулы «Омега-3» 1000 мг, 200 шт.",
            20);
        INSERT INTO Products (title, description, price) VALUES (
            "PQQ Energy",
            "Пирролохинолинхинон, 30 шт.",
            30);
    ''')
    connection.commit()
    connection.close()  # Закрываем соединение после выполнения


def get_all_products():
    connection = sqlite3.connect('products.db')  # Новое подключение
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.close()  # Закрываем соединение после выполнения
    return products


if __name__ == '__main__':
    initiate_db()
    populate_db()
