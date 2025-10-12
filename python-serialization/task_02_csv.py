#!/usr/bin/env python3
"""CSV to JSON conversion module"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV data to JSON format"""
    try:
        # Read CSV file and convert to list of dictionaries
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)
        
        # Write JSON data to data.json
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    except Exception:
        return False
