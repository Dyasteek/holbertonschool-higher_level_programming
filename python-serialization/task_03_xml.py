#!/usr/bin/env python3
"""XML serialization module"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize dictionary to XML"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize XML to dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary
