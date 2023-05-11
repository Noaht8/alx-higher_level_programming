#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return (str)
    if len(str) < n or n < 0:
        return (str)
    str = str.replace(str[n], '')
    return str
