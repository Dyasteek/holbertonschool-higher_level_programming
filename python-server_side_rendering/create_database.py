#!/usr/bin/env python3
"""
Script to create and populate the products.db SQLite database.
Run this script once to set up the database for Task 04.
"""

import sqlite3


def create_database():
    """Create and populate the products database."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Insert data
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')

    conn.commit()
    conn.close()
    print("Database created successfully!")


if __name__ == '__main__':
    create_database()

