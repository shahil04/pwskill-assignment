# 7. Integrate a SQLite database with Flask to perform CRUD operations on a list of items.

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'Q7_intigrate_sqlite_and_perform_curd\items.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def init_db():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
                CREATE TABLE IF  NOT EXISTS items
                       (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL         
                       )               
                       ''')
        conn.commit()


@app.route("/")
def index():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items")
        items = cursor.fetchall()
    
    return render_template('index.html', items=items)


@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO items (name) VALUES (?)", (name,))
            conn.commit()
        return redirect(url_for('index'))
    return render_template('add_item.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    if request.method == 'POST':
        name = request.form['name']
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE items SET name = ? WHERE id = ?", (name, id))
            conn.commit()
        return redirect(url_for('index'))
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items WHERE id = ?", (id,))
        item = cursor.fetchone()
    return render_template('edit_item.html', item=item)

@app.route('/delete/<int:id>')
def delete_item(id):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM items WHERE id = ?", (id,))
        conn.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
