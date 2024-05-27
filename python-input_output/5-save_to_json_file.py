#!/usr/bin/python3
"""save_to_json_file module.

Contains a function that writes an Object to a text file.
"""
import json

def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation."""
    try:
        with open(filename, 'w') as f:
            json.dump(my_obj, f)
    except TypeError as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    except PermissionError as e:
        print("[{}] {}".format(e.__class__.__name__, e))

