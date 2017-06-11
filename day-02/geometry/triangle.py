class Triangle:
	def __init__(self, bottom, height):
		self.bottom = bottom
		self.height = height

	def triangle_area(self):
		formula = self.bottom * self.height / 2
		return formula