import math

class Point:
    def __init__(self, x ,y):
        self.x = x
        self.y = y
    def distance_from_origin(self):
        return math.hypot(self.x, self.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        else :
            return self.y < other.y
    def __str__(self):
        return "({0.x:.3f},{0.y:.3f})".format(self)
    def __repr__(self):
        return "Point({0.x},{0.y})".format(self)

a = Point(3, 5)
b = Point(3, 5)
c = Point(3, 6)

print(b.distance_from_origin())
print(b == a)
print(a < c)
print(a is b)
print(isinstance(a, Point))
p = eval(repr(a))
print(p==a)
print(p is a)
print(p)
