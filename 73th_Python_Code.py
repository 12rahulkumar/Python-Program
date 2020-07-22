class employee:

	def __init__(self):
		self.eno = 100
		self.ename = "rahul"
		self.esal = 10000

e = employee()
print(e.__dict__)