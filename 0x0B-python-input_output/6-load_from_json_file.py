#!/usr/bin/python3
"""save_to_json_file module.

Contains a function that creates an Object from a “JSON file”.
"""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”."""
    with open(filename, 'r') as f:
        return json.load(f)
