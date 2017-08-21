import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        formula = math.pi * self.radius ** 2
        return formula
