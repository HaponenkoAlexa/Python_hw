class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.square == other.square

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.width + other.width, self.height + other.height)
        else:
            raise TypeError("Unsupported operand type for +: 'Rectangle' and {}".format(type(other)))

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            return Rectangle(self.square, n)
        else:
            raise TypeError("Unsupported operand type for *: 'Rectangle' and {}".format(type(n)))

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)


# Перевірка
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

assert r1.square == 8, 'Test1'
assert r2.square == 18, 'Test2'

r3 = r1 + r2
assert r3.square == 50, 'Test3'

r4 = r1 * 4
assert r4.square == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

print("ОК")

