class Triangle:
	COUNT = 0

	def __init__(self, bottom, height):
		self.bottom = bottom
		self.height = height
		Triangle.COUNT = Triangle.COUNT + 1

	def triangle_area(self):
		formula = self.bottom * self.height / 2
		return formula