import unittest

import perimeter


class TestPerimeter(unittest.TestCase):

    def test_perimeter(self):
        return self.assertEqual(perimeter.rectangle_perimeter(3, 4), 14)

    @unittest.skip('Skipped ValueError Test')
    def test_error(self):
        with self.assertRaises(ValueError):
            perimeter.rectangle_perimeter(3, 4)


if __name__ == '__main__':
    unittest.main()
