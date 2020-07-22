class test:

	def __init__(self):
		self.a = 10
		self.b = 30
		self.c = 40

t1 = test()
t2 = test()
t1.b = 9989
t2.a = 12

print(t1.__dict__)
print(t2.__dict__)