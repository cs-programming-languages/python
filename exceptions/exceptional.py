"""Module for demonstrating exceptions

"""
import sys
from math import log

def convert(s):
    """Covnert to integer"""

    try:
        return int(s)
    except (ValueError, TypeError) as e:         # Tuple of exception types
        print("Convertion error: {}".format(str(e)),file=sys.stderr)
        raise

def string_log(s):
    v = convert(s)
    return log(v)