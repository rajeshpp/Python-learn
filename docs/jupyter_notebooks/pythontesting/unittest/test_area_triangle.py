import unittest

import areas


class TestArea(unittest.TestCase):

    def test_triangle(self):
        result = areas.triangle(10, 5)
        self.assertEqual(result, 25)


if __name__ == '__main__':
    unittest.main()
