import sys
import unittest

import perimeter


class TestPerimeter(unittest.TestCase):

    def test_perimeter(self):
        return self.assertEqual(perimeter.rectangle_perimeter(3, 4), 14)

    @unittest.skipIf(sys.version_info[0] < 3, 'Python Version 3 or more required.')
    def test_error(self):
        with self.assertRaises(ValueError):
            perimeter.rectangle_perimeter(3, 0)


if __name__ == '__main__':
    unittest.main()
