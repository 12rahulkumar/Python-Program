class student:
	"'document by durga for python demo'"

	def __init__(self):
		self.name = 'rahul'
		self.age = 22
		self.marks = 33

	def talk(self):
		print('hello i am ',self.name)
		print('my age is ',self.age)
		print('my marks is ',self.marks)

s = student()
s.talk()