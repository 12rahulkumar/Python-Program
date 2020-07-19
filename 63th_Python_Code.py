class test:

	a = 10
	def __init__(self):
		test.b = 20

	def m1(self):
		test.c = 30

	def m2(cls):
		cls.d1 = 40
		test.d2 = 50

	def m3():
		test.e = 60

print(test.__dict__)
t=test()
print(test.__dict__)
t.m1()
print(test.__dict__)
test.m2()
print(test.__dict__)
test.m3()
print(test.__dict__)
test.f=60
print(test.__dict__) 

