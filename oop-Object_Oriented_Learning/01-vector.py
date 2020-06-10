class Vec:
    def __init__(self, x = 0, y = 0):
        self.x, self.y = x, y
    def dot(self, other):
        return self.x*other.x+self.y*other.y
    def sca(self, scalar):
        return Vec(self.x*scalar, self.y*scalar)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        return "Vec({0.x!r}, {0.y!r})".format(self)
    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)
    def __abs__(self):
        return self.dot(self)**0.5
    def __bool__(self):
        return bool(abs(self))
    def __add__(self, other):
        return Vec(self.x+other.x, self.y+other.y)
    def __sub__(self, other):
        return Vec(self.x-other.x, self.y-other.y)
    def __mul__(self, other):
        return self.dot(other) if isinstance(other, Vec) else self.sca(other)
