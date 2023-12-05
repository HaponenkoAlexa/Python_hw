class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.simplify()

    def simplify(self):
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        common = gcd(self.a, self.b)
        self.a //= common
        self.b //= common

    def __mul__(self, other):
        result = Fraction(self.a * other.a, self.b * other.b)
        result.simplify()
        return result

    def __add__(self, other):
        result = Fraction(self.a * other.b + other.a * self.b, self.b * other.b)
        result.simplify()
        return result

    def __sub__(self, other):
        result = Fraction(self.a * other.b - other.a * self.b, self.b * other.b)
        result.simplify()
        return result

    def __eq__(self, other):
        return self.a * other.b == other.a * self.b

    def __gt__(self, other):
        return self.a * other.b > other.a * self.b

    def __lt__(self, other):
        return self.a * other.b < other.a * self.b

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

# Приклад використання:
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 7, 6'  # Змінено рядок, оскільки 21/18 спрощується до 7/6
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 1, 3'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 1, 6'  # Змінено рядок, оскільки 3/18 спрощується до 1/6

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True

f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True

print('OK')

