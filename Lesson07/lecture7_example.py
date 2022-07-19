class Human(object):
	name = None
	sex = None
	birth_year = None

	def __init__(self, name, year):
		self.name = name
		self.birth_year = year

	def get_age(self):
		if type(self.birth_year) == int:
			return 2022 - self.birth_year
		return None

class Student(Human):
	vuz = None
	marks = []

	def __init__(self, name, year, marks):
		self.name = name
		self.birth_year = year
		self.marks = marks

	def get_average_mark(self):
		if len(self.marks):
			return 1.0 * sum(self.marks) / len(self.marks)
		return 0