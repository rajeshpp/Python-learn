import unittest

import perimeter


class TestPerimeter(unittest.TestCase):

    def test_perimeter(self):
        return self.assertEqual(perimeter.rectangle_perimeter(3, 4), 14)

    def test_error(self):
        return self.assertRaises(ValueError, perimeter.rectangle_perimeter, 3, 0)


if __name__ == '__main__':
    unittest.main()
