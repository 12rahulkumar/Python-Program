class student:

	def __init__(self,name,age,marks):
		self.name = name
		self.age = age
		self.marks = marks

	def talk(self):
		print('i am ',self.name)
		print('my age is ',self.age)
		print('my marks is ',self.marks)


# to cretae object
s = student("rahul",20,80)
s.talk()