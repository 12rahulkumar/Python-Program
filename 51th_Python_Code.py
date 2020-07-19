# data can be represented by a variable

# in python we have 3 types of variables inside a class
#---> instance variable
#---> static variable
#---> local variable

# in python we have 3 types of methods inside a class
#---> instance method
#---> static method
#---> class method

class student:
	"'developed by rahul'"

	def __init__(self):
		self.name = 'rahul'
		self.age = 22
		self.marks = 80

	def talk(self):
		print('hello i am',self.name)
		print('my age is ',self.age)
		print('my marks us ',self.marks)

# syntax to create object
# reference variable = classname()

s = student()
