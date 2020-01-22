#!/usr/bin/python3
"""
   Name Module: 9-add_item
   Description: Module that adds all arguments to a Python list,
                and then save them to a file
"""
import json
import sys


load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

filename = "add_item.json"

try:
    lista = load_from_json_file(filename)
except Exception:
    lista = []

for i, j in enumerate(sys.argv):
    if i == 0:
        continue
    lista.append(j)

save_to_json_file(lista, filename)
