"""
Program: compound_expressions.py
Author: Ryan Elliott
Last date modified: 06/10/2020
"""

if __name__ == '__main__':
    MAX = 10
    MIN = 0
    y = 12
    if y > MAX:
        print("y is greater than MAX")
    else:
        print("y is less than MAX")
    if y < MIN:
        print("y is less than MIN")
    else:
        print("y is greater than MIN")
    x = 4
    if MIN < x < MAX:
        print("x is between MIN and MAX")
    else:
        print("x is not between MIN and MAX")
    if MIN <= x < MAX:
        print("x is greater than or equal to MIN and less than MAX")
    else:
        print("x is not less than or equal to MIN and less than MAX")
    if MIN < x <= MAX:
        print("x is greater than MIN and less than or equal to MAX")
    else:
        print("x is not greater than MIN and less than or equal to MAX")
