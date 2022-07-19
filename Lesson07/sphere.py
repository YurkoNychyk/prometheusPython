import math

class Sphere(object):
	"""docstring for Sphere"""


	def __init__(self, r = 1.0, x = 0.0, y = 0.0, z = 0.0):
		self.r = r * 1.0
		self.x = x * 1.0
		self.y = y * 1.0
		self.z = z * 1.0

	def print_sphere(self):
		print("R = %d, X = %d, Y =%d, Z =%d" % (self.r, self.x, self.y, self.z))	

	def get_center(self):
		return (self.x, self.y, self.z)

	def get_volume(self):
		return math.pow(self.r, 3) *  math.pi * 4.0 / 3

	def get_square(self):
		return 4 * math.pi * math.pow(self.r,2) 	

	def get_radius(self):
		return self.r


	def is_point_inside(self, x, y ,z):

		print ("point is: %2.1f, %2.1f, %2.1f, sphere is %2.1f, %2.1f, %2.1f, radius: %2f" % (x*1.0,y*1.0,z*1.0, self.x, self.y, self.z, self.r))

		if math.fabs(x * 1.0) <= (math.fabs(self.x) + self.r) and math.fabs(y*1.0) <= (math.fabs(self.y) + self.r) and math.fabs(z*1.0) <= (math.fabs(self.z) + self.r) :
			return True
		else:
			return False


	def set_radius(self, r):
		self.r = r * 1.0

	def set_center(self, x, y, z):
		self.x = 1.0 * x
		self.y = 1.0 * y
		self.z = 1.0 * z