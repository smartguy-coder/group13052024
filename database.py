import sqlite3
import hashlib
from pprint import pprint


DB_PATH = 'our_db_13052024.sqlite3'


def encript_password(value: str) -> str:
    hashed = hashlib.md5(value.encode()).hexdigest()
    return hashed


with sqlite3.connect(DB_PATH) as connection:
    cursor = connection.cursor()
    connection.create_function('encode', 1, encript_password)

    # create table
    # query = """
    #     CREATE TABLE IF NOT EXISTS category(
    #         id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #         name VARCHAR(20) NOT NULL,
    #         description TEXT,
    #         segment VARCHAR(20)
    #     )
    # """
    # cursor.execute(query)

    # add column
    # query = """
    #     ALTER TABLE category
    #     ADD COLUMN segment VARCHAR(20)
    # """
    # cursor.execute(query)

    # CREATE DATA
    # hardcode
    # query = """
    #     INSERT INTO category(name, description, segment)
    #     VALUES ('DELL500', 'old stuff', 'sale')
    # """
    # cursor.execute(query)
    # dynamic data
    # name = 'kinetic sand red one'
    # description = "injection', '8888888')--"
    # segment = 'junior'
    # warning
    # query = f"""
    #     INSERT INTO category(name, description, segment)
    #     VALUES ('{name}', '{description}', '{segment}')
    # """
    # cursor.execute(query)

    # DO this way
    # values = [name, description, segment]
    # query = """
    #     INSERT INTO category(name, description, segment)
    #     VALUES (?, ?, ?)
    # """
    # cursor.execute(query, values)

    # query = """
    #     CREATE TABLE IF NOT EXISTS products(
    #         id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #         title TEXT NOT NULL UNIQUE,
    #         whole_price DECIMAL(10, 2) CHECK (whole_price > 0),
    #         price DECIMAL(10, 2) CHECK (price >= whole_price),
    #         category_id INTEGER,
    #         FOREIGN KEY (category_id) REFERENCES category(id)
    #     );
    #     CREATE TABLE IF NOT EXISTS user(
    #         id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #         name TEXT NOT NULL,
    #         login TEXT NOT NULL CHECK (length(login) > 3) UNIQUE,
    #         password TEXT NOT NULL,
    #         address TEXT
    #     )
    # """
    # cursor.executescript(query)


    # values = (
    #     ('Dell 500', 600, 2500, 1),
    #     ('Dell 800', 1777, 8888, 1),
    #     ('Dell 6500', 77, 90, 1),
    # )
    # query = """
    #     INSERT INTO products(title, whole_price, price, category_id)
    #     VALUES (?, ?, ?, ?)
    # """
    # cursor.executemany(query, values)
    # user_name = 'Igor'
    # login = 'casper184'
    # password = 'termos'
    # values = [user_name, login, password]
    # query = """
    #     INSERT INTO user(name, login, password)
    #     VALUES (?, ?, encode(?))
    # """
    # cursor.execute(query, values)

    # READ
    # query = """
    #     SELECT title, price, 2 + 2 as co
    #     FROM products
    # """
    # result = cursor.execute(query)
    # pprint(result.fetchall(), width=40)

    # query = """
    #     SELECT title, price
    #     FROM products
    #     WHERE id >= 2
    # """
    # result = cursor.execute(query)
    # pprint(result.fetchall(), width=40)

    # query = """
    #     SELECT title, price
    #     FROM products
    #     WHERE id < 5 AND price > 1000
    # """
    # result = cursor.execute(query)
    # pprint(result.fetchall(), width=40)

    # query = """
    #     SELECT id, title, price
    #     FROM products
    #     WHERE id < 5 OR (price > 1000 AND title LIKE 'Samsung___%')
    # """
    # result = cursor.execute(query)
    # pprint(result.fetchall(), width=40)

    # query = """
    #     SELECT products.id, products.title, products.price, category.name
    #     FROM products
    #     LEFT JOIN category
    #     ON products.category_id = category.id
    #
    #
    #     WHERE (products.id BETWEEN 2 AND 6) OR (category.id = 1)
    #     ORDER BY products.id DESC
    #     LIMIT 3
    #     OFFSET 3
    # """
    # result = cursor.execute(query)
    # pprint(result.fetchall(), width=80)

    # query = """
    #     SELECT products.id, products.title, products.price, category.name, category.id
    #     FROM products
    #     INNER JOIN category
    #     ON products.category_id = category.id
    #
    # """
    # result = cursor.execute(query)
    # pprint(result.fetchall(), width=80)

    # UPDATE
    # Update table data
    # query = """
    #     UPDATE products
    #     SET
    #         title = 'NOKIA'
    #     WHERE id = 5
    # """
    # cursor.execute(query)

    query = """
        UPDATE products
        SET
            title = LOWER(:Name || '_' || 'China'),
            price = :Price
        WHERE id = :Id
    """
    cursor.execute(query, {'Name': 'POKO', 'Price': 10000, 'Id': 5})

    # RENAME TABLE
    # query = """
    #     ALTER TABLE user
    #     RENAME TO customers
    # """
    # cursor.execute(query)
    # RENAME COLUMN
    # query = """
    #     ALTER TABLE customers
    #     RENAME COLUMN name TO user_name
    # """
    # cursor.execute(query)

    # DELETE
    # query = """
    #     DELETE FROM products
    #     WHERE id = 10
    # """
    # result = cursor.execute(query)
    # print(result.fetchall())

    # DUMP
    # CREATE DUMP
    # with open("dump.sql", 'w') as dump:
    #     for sql in connection.iterdump():
    #         dump.write(sql)

    # with open("dump.sql", 'r') as dump:
    #     sql = dump.read()
    #     cursor.executescript(sql)

    # TRIGGERS
    # trigger = """
    #     CREATE TRIGGER IF NOT EXISTS discount_in_title
    #     AFTER UPDATE ON products
    #     WHEN old.price > new.price
    #     BEGIN
    #         UPDATE products
    #         SET title = title || UPPER('- with discount >> ') || new.price
    #         WHERE id = new.id;
    #     END;
    # """
    # cursor.execute(trigger)
