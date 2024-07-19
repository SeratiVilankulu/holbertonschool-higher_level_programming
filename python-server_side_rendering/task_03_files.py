from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def read_csv_file(file_path):
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['price'] = float(row['price'])  # Convert price to float
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error = None
    
    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    else:
        error = "Wrong source"
    
    if error is None:
        if product_id:
            products = [p for p in products if str(p['id']) == product_id]
            if not products:
                error = "Product not found"
    
    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True)
