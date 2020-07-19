class student:
	"'this is student class with required data'"

	def __init__(self,name,roll,marks):
		self.name = name
		self.roll = roll
		self.marks = marks

	def display(self):
		print('i am ',self.name)
		print('my roll number is ',self.roll)
		print('my marks is ',self.marks)

s1 = student("rahul",101,80)
s1.display()
s2 = student("sumit",221,11)
s2.display()
s2.display()