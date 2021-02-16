import unittest


class Testing(unittest.TestCase):

    def test_string(self):
        x = 'Alpha'
        y = 'Alpha'

        self.assertEqual(x, y)


if __name__ == '__main__':
    unittest.main()
