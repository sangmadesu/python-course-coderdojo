"""
Main program
"""
from triangle import triangle_area as triangle
from square import square_area as square
from circle import circle_area as circle

print('Main Application To Calculate Geometry Area For: Circle, Square, Triangle')

tr1 = triangle(5, 4)
print tr1
sqr1 = square(4)
print sqr1
cir1 = circle(5)
print cir1
