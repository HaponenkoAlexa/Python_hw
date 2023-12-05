class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        new_width = max(self.width, other.width)
        new_height = max(self.height, other.height)
        return Rectangle(new_width, new_height)

    def __mul__(self, n):
        return Rectangle(self.width * n, self.height * n)

    def __str__(self):
        return f'Rectangle: width={self.width}, height={self.height}, square={self.get_square()}'


# Тестування
r1 = Rectangle(2, 4)
r4 = r1 * 2  # Adjust the multiplier to 2
assert r4.get_square() == 16, 'Test4'  # Corrected value

print(r1)
print(r4)
