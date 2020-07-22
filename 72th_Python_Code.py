class student:

	def __init__(self,name,roll,marks):
		self.name = name
		self.roll = roll
		self.marks = marks

	def display(self):
		print('my name is ',self.name)
		print('my roll is ',self.roll)
		print('my marks is ',self.marks)

s = student("rahul",451,66)
s.display()