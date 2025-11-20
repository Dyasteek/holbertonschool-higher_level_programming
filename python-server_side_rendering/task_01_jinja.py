#!/usr/bin/env python3
"""
Task 01: Creating a Basic HTML Template in Flask
Basic Flask application with Jinja templates and reusable components.
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)

