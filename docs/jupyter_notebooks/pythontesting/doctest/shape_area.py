"""
>>> triangle(4, 3)
6.0
>>> rectangle(4, 3)
12
>>> square(5)
25
"""
def triangle(height, base):
    return 0.5 * height * base

def rectangle(length, breadth):
    return length * breadth

def square(side):
    return side**2


'''
>>> python -m doctest shape_area.py -v

Trying:
    triangle(4, 3)
Expecting:
    6.0
ok
Trying:
    rectangle(4, 3)
Expecting:
    12
ok
Trying:
    square(5)
Expecting:
    25
ok
3 items had no tests:
    shape_area.rectangle
    shape_area.square
    shape_area.triangle
1 items passed all tests:
   3 tests in shape_area
3 tests in 4 items.
3 passed and 0 failed.
Test passed.

'''