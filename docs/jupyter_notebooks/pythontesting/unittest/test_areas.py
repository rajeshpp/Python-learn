import unittest

import areas


class TestArea(unittest.TestCase):
    def test_triangle(self):
        self.assertEqual(areas.triangle(10, 5), 25)

    def test_rectangle(self):
        self.assertEqual(areas.rectangle(10, 5), 50)

    def test_square(self):
        self.assertEqual(areas.square(5), 25)


if __name__ == '__main__':
    unittest.main()

"""
>>> python test_areas.py
>>> python -m unittest test_areas.py
>>> python -m unittest test_areas.TestArea.test_square
>>> python -m unittest test_areas.TestArea.test_square test_areas.TestArea.test_rectangle
"""
