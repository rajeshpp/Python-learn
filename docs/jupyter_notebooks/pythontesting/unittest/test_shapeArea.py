from unittest import TestCase
import shape_area

class TestShapeArea(TestCase):
    def test_triangle(self):
        self.assertEqual(shape_area.ShapeArea.triangle(10, 5), 25)

    def test_rectangle(self):
        self.assertEqual(shape_area.ShapeArea.rectangle(10, 5), 50)

    def test_square(self):
        self.assertEqual(shape_area.ShapeArea.square(10), 100)
