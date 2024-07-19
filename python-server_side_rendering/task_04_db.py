from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json():
    try:
        with open('items.json') as file:
            data = json.load(file)
            return data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv():
    items = []
    try:
        with open('items.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                items.append(row)
    except FileNotFoundError:
        pass
    return items

def read_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT name, category, price FROM Products')
        rows = cursor.fetchall()
        conn.close()
        return [{'name': row[0], 'category': row[1], 'price': row[2]} for row in rows]
    except sqlite3.Error:
        return []

@app.route('/products')
def products():
    source = request.args.get('source', 'json')
    
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sql()
    else:
        return "Wrong source", 400

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
