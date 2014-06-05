#!/usr/bin/python
"""
Reindent NDB objects dumps to be human readable
"""
import sys


def parse(data):
    """
    Parse data
    """
    indentation = 0
    toDisplay = ''

    for char in data:
        if char == '(' or char == '[':
            print "%s%s%s" % ('    ' * indentation, toDisplay.strip(), char)
            indentation = indentation + 1
            toDisplay = ''
        elif char == ')' or char == ']':
            print "%s%s" % ('    ' * indentation, toDisplay.strip())
            indentation = indentation - 1
            toDisplay = char
        elif char == ',':
            print "%s%s%s" % ('    ' * indentation, toDisplay.strip(), char)
            toDisplay = ''
        elif char == '\n':
            pass
        else:
            toDisplay = toDisplay + char

    if toDisplay != '':
        print toDisplay.strip()

if __name__ == '__main__':
    parse(sys.argv[1])
