# Program to demonistrate constructor will execute only once per object:

class test:

	def __init__(self):
		print('constructor is called')

	def m1(self):
		print('method execute')

t1 = test()
t2 = test()
t3 = test()
# t4 = t4.m1() error
t1.m1()