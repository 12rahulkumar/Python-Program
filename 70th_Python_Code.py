class student:

	def __init__(self,name,age,marks):
		self.name = name
		self.age = age
		self.marks = marks

	def talk(self):
		print('hii i  am ',self.name)
		print('my age is ',self.age)
		print('my marks is ',self.marks)

s = student('rahul',23,55)
s.talk()
print(s.name)