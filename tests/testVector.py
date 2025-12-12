from ..solutions.utils.vectors import Point, Vector
import pytest

@pytest.fixture
def setUp():
    a = Point(0, 0)
    b = Point(0, 3)
    c = Point(3, 0)
    ab = Vector(a, b)
    ac = Vector(a, c)
    yield ab, ac
    
def testLen(setUp):
    assert(ab.magnitude== 3)
