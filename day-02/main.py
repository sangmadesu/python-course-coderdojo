"""
Main program
"""
from geometry.triangle import Triangle
from geometry.circle import Circle
from geometry.square import Square

print('Main Application To Calculate Geometry Area For: Circle, Square, Triangle')
tr1 = Triangle(5,4)
print tr1.triangle_area()
cir1 = Circle(10)
print cir1.circle_area()
sqr1 = Square(4)
print sqr1.square_area()
