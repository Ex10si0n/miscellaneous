from 02-vector import Vec

class Mat:
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d
    def __eq__(self, other):
        if self.a == other.a and self.b == other.b and self.c == other.c and self.d == other.d:
            return True
        return False
    def __hash__(self):
        return hash(self.a, self.b, self.c, self.d)
    def __repr__(self):
        return "Mat[({0.a!r}, {0.b!r}), ({0.c!r}, {0.d!r})]".format(self)
    def __str__(self):
        return "[({0.a!r}, {0.b!r}), ({0.c!r}, {0.d!r})]".format(self)
    def __add__(self, other):
        return Mat(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)
    def __neg__(self):
        return Mat(-self.a, -self.b, -self.c, -self.d)
    def __sub__(self, other):
        return self + -other
    def mul_by_vec(self, other):
        return Vec(self.a * other. x + self.b * other.y, self.c * other. x + self.d * other.y)
    def mul_by_mat(self, other):
        return Mat(self.a * other.a + self.b * other.c, self.a * other.b + self.b * other.d, \
            self.c * other.a + self.d * other.c, self.c * other.b + self.d * other.d)
    def __mul__(self, other):
        return self.mul_by_vec(other) if isinstance(other, Vec) else self.mul_by_mat(other)
    def __pow__(self, n):
        r = Mat(1, 0, 0, 1)
        s = self
        while n > 0:
            if n % 2 == 1:
                r = r * s
            s = s * s
            n //= 2
        return r


        