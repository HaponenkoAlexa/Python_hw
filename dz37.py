class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return (self.width, self.height) == (other.width, other.height)

    def __add__(self, other):
        if isinstance(other, Rectangle):
            width_sum = self.width + other.width
            height_sum = self.height + other.height
            return Rectangle(width_sum, height_sum)
        else:
            raise ValueError("Unsupported operand type for +: {}".format(type(other)))

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            return Rectangle(self.width * n, self.height * n)
        else:
            raise ValueError("Unsupported operand type for *: {}".format(type(n)))

    def __str__(self):
        return f"Rectangle: width={self.width}, height={self.height}"


# Приклад використання:
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'
