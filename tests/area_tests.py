import pytest

from area.area import Triangle, Circle


@pytest.fixture
def right_triangle():
    return Triangle(3, 4, 5)


@pytest.fixture()
def triangle():
    return Triangle(1, 3, 4)


@pytest.fixture()
def circle():
    return Circle(1)


def test_triangle_init(right_triangle):
    assert right_triangle.a == 3
    assert right_triangle.b == 4
    assert right_triangle.c == 5


def test_triangle_area(right_triangle):
    assert right_triangle.area() == 6


def test_triangle_is_right(right_triangle, triangle):
    assert right_triangle.is_right()
    assert not triangle.is_right()


def test_circle_init(circle):
    assert circle.r == 1


def test_circle_area(circle):
    assert round(circle.area(), 2) == 3.14
