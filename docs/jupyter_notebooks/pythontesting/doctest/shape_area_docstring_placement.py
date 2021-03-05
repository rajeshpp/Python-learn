"""
>>> triangle(6, 7)
21.0
"""
def triangle(height, base):
    """
    >>> triangle(4, 3)
    6.0
    """
    return 0.5 * height * base


def rectangle(length, breadth):
    """
    >>> rectangle(4, 3)
    12
    """
    return length * breadth


def square(side):
    """
    >>> square(5)
    25
    """
    return side**2

'''
>>> python -m doctest shape_area_docstring_placement.py -v

Trying:
    triangle(6, 7)
Expecting:
    21.0
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
Trying:
    triangle(4, 3)
Expecting:
    6.0
ok
4 items passed all tests:
   1 tests in shape_area_docstring_placement
   1 tests in shape_area_docstring_placement.rectangle
   1 tests in shape_area_docstring_placement.square
   1 tests in shape_area_docstring_placement.triangle
4 tests in 4 items.
4 passed and 0 failed.
Test passed.


>>> python -m pytest --doctest-modules shape_area_docstring_placement.py -v

shape_area_docstring_placement.py::shape_area_docstring_placement PASSED [ 25%]
shape_area_docstring_placement.py::shape_area_docstring_placement.rectangle PASSED [ 50%]
shape_area_docstring_placement.py::shape_area_docstring_placement.square PASSED [ 75%]
shape_area_docstring_placement.py::shape_area_docstring_placement.triangle PASSED [100%]


>>> python -m unittest shape_area_docstring_placement.py -v

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
###Refer: test_docstring_unittest.py
'''