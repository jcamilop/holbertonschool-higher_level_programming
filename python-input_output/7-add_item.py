#!/usr/bin/python3
"""script that adds all arguments to a Python list"""
from sys import argv
import json

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

fileName = "add_item.json"

try:
    json_list = load_from_json_file(fileName)
except Exception:
    json_list = []

for arg in argv[1:]:
    json_list.append(arg)

save_to_json_file(json_list, fileName)
