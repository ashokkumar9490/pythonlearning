import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"area of circle with radius {self.radius} is {round(self.calculate_area(), 2)}"

    def calculate_area(self):
        return math.pi * self.radius * self.radius


c1 = Circle(5)
c2 = Circle(10)

print(c1)
print(c2)
