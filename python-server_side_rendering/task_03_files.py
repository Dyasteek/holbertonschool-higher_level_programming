#!/usr/bin/env python3
"""
Task 03: Displaying Data from JSON or CSV Files in Flask
Flask application that reads and displays product data from JSON or CSV files.
"""

import csv
import json
import os
from flask import Flask, render_template, request


app = Flask(__name__)


def read_products_from_json():
    """
    Read products from products.json file.

    Returns:
        list: List of product dictionaries
    """
    json_file = 'products.json'
    if not os.path.exists(json_file):
        return []

    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, IOError):
        return []


def read_products_from_csv():
    """
    Read products from products.csv file.

    Returns:
        list: List of product dictionaries
    """
    csv_file = 'products.csv'
    if not os.path.exists(csv_file):
        return []

    products = []
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert id and price to appropriate types
                product = {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                products.append(product)
    except (ValueError, IOError, KeyError):
        return []

    return products


def filter_product_by_id(products, product_id):
    """
    Filter products list by id.

    Args:
        products (list): List of product dictionaries
        product_id (int): Product ID to filter by

    Returns:
        dict or None: Product dictionary if found, None otherwise
    """
    for product in products:
        if product.get('id') == product_id:
            return product
    return None


@app.route('/products')
def products():
    """
    Display products from JSON or CSV based on source query parameter.
    Optionally filter by id query parameter.
    """
    source = request.args.get('source', '').lower()
    product_id_param = request.args.get('id')

    products_list = []
    error_message = None

    # Determine data source
    if source == 'json':
        products_list = read_products_from_json()
    elif source == 'csv':
        products_list = read_products_from_csv()
    else:
        error_message = "Wrong source"
        return render_template('product_display.html',
                             products=None,
                             error_message=error_message)

    # Filter by id if provided
    if product_id_param:
        try:
            product_id = int(product_id_param)
            found_product = filter_product_by_id(products_list, product_id)
            if found_product:
                products_list = [found_product]
            else:
                error_message = "Product not found"
                products_list = []
        except ValueError:
            error_message = "Product not found"
            products_list = []

    return render_template('product_display.html',
                         products=products_list,
                         error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

