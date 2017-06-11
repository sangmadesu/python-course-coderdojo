"""
Main program
"""
from geometry.triangle import Triangle
from geometry.circle import Circle
from geometry.square import Square

print('Main Application To Calculate Geometry Area For: Circle, Square, Triangle')
tr1 = Triangle(10, 5)
print 'Jumlah segitiga', tr1.COUNT, 'adalah', tr1.triangle_area()

tr2 = Triangle(30, 5)
print 'Jumlah segitiga', tr2.COUNT, 'adalah', tr2.triangle_area()

# cir1 = Circle(10)
# print cir1.circle_area()

# sqr1 = Square(4)
# print sqr1.square_area()
