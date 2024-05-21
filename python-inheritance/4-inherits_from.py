#!/usr/bin/python3
"""
Contains the inherits_from function.
"""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a class that inherited (directly or
    indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a class that inherited from a_class,
        but is not an instance of a_class itself. False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
