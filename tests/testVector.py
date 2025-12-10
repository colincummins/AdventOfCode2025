from ..solutions.utils.vectors import Point, Vector
import unittest

class TestVector(unittest.TestCase):
    def setUp(self):
        a = Point(0, 0)
        b = Point(0, 3)
        c = Point(3, 0)
        self.ab = Vector(a, b)
        self.ac = Vector(a, c)
    
    def testLen(self) -> None:
        self.assertEqual(self.ab.magnitude, 3)
        self.assertEqual(self.ab.magnitude, 3)

if __name__ == "main":
    unittest.main()