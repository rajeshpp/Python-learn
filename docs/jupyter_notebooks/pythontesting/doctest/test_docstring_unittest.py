import shape_area_docstring_placement as shape_area

import unittest
import doctest

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(shape_area))
    return tests


'''
>>> python -m unittest test_docstring_unittest.py -v

rectangle (shape_area_docstring_placement)
Doctest: shape_area_docstring_placement.rectangle ... ok
square (shape_area_docstring_placement)
Doctest: shape_area_docstring_placement.square ... ok
triangle (shape_area_docstring_placement)
Doctest: shape_area_docstring_placement.triangle ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.168s

OK

'''