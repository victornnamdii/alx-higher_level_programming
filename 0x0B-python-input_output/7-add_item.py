#!/usr/bin/python3
"""
A script that adds all arguments to a Python list,
and then save them to a file
"""


import sys
import os.path
import json
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
json_list = []

if os.path.exists(filename):
    json_list = load(filename)

for i in range(1, len(sys.argv)):
    json_list.append(sys.argv[i])

save(json_list, filename)
