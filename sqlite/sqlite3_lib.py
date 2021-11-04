import os
import sqlite3

def setup_db():
    os.remove('example.db')
    con = sqlite3.connect('example.db')
    cursor = con.cursor()
    return con, cursor

def simple_example():
    con, cursor = setup_db()
    cursor.execute('CREATE TABLE books (title text, author text, price real, quantity integer);')
    for book_info in [('Great Expectations', 'Charles Dickens', 10.99, 2),
                      ('Crime and Punishment', 'Fyodor Dostoevsky', 27.95, 4),
                      ('Twilight', 'Stephanie Meyer', 4.99, 57),
                      ('What If?', 'Randall Munroe', 24.0, 5)]:
        cursor.execute('INSERT INTO books VALUES (?, ?, ?, ?);', book_info)

    for row in cursor.execute('SELECT * FROM books WHERE price > 20.0;'):
        print(row)

    con.commit()
    con.close()

def relational_example():
    con, cursor = setup_db()
    cursor.execute('''CREATE TABLE authors (id integer PRIMARY KEY,
                                            name text,
                                            born integer NOT NULL,
                                            died integer);''')
    cursor.execute('''CREATE TABLE books (id integer PRIMARY KEY,
                                          title text,
                                          author_id integer,
                                          price real,
                                          year integer,
                                          quantity integer,
                                          FOREIGN KEY(author_id) REFERENCES authors(id));''')

    for author_info in [('Charles Dickens', 1812, 1870),
                        ('Fyodor Dostoevsky', 1821, 1881),
                        ('Stephanie Meyer', 1973, None),
                        ('Randall Munroe', 1984, None)]:
        cursor.execute('INSERT INTO authors (name, born, died) VALUES (?, ?, ?)', author_info)

    for author_name, book_info in [
        ('Charles Dickens', ('Great Expectations', 10.99, 1861, 2)),
        ('Fyodor Dostoevsky', ('Crime and Punishment', 27.95, 1866, 4)),
        ('Stephanie Meyer', ('Twilight', 4.99, 2005, 57)),
        ('Randall Munroe', ('What If?', 24.0, 2014, 5))]:
        cursor.execute('''INSERT INTO books (author_id, title, price, year, quantity)
VALUES ((SELECT id FROM authors WHERE name = ?), ?, ?, ?, ?);''', (author_name,) + book_info)

    for row in cursor.execute('''SELECT title, price, name FROM books JOIN authors ON author_id = authors.id
WHERE authors.died IS NOT NULL;'''):
        print(row)

    con.commit()
    con.close()

if __name__ == '__main__':
    relational_example()
