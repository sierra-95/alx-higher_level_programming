#!/usr/bin/python3
def safe_print_integer(value):
    try:
        int(value)
        print("{}".format(value),end="")
        print()
        return True
    except ValueError:
        return False