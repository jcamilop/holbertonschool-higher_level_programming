#!/usr/bin/python3
"""Module for import load_from_json_file"""

import json


def load_from_json_file(filename):
    """Creates an object"""
    with open(filename, 'r') as f:
        return json.load(f)
