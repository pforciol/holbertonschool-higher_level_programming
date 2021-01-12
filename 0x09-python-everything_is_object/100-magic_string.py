#!/usr/bin/python3
def magic_string(static={"count": 0}):
    static["count"] += 1
    return str("Holberton, " * static["count"])[:-2]
