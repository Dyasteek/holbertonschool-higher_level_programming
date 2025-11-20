#!/usr/bin/env python3
"""
Task 02: Creating a Dynamic Template with Loops and Conditions in Flask
Flask application with dynamic content using Jinja loops and conditionals.
"""

import json
import os
from flask import Flask, render_template


app = Flask(__name__)


def load_items_from_json():
    """
    Load items from items.json file.

    Returns:
        list: List of items, or empty list if file doesn't exist or is invalid
    """
    json_file = 'items.json'
    if not os.path.exists(json_file):
        return []

    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data.get('items', [])
    except (json.JSONDecodeError, IOError) as e:
        return []


@app.route('/items')
def items():
    """Render the items page with dynamic content from JSON."""
    items_list = load_items_from_json()
    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

