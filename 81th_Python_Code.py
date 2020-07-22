import sys

class Customer:
	"'Customer class with bank operations'"

	bankname = "punjab national bank"

	def __init__(self,name,balance = 0.0):
		self.name = name
		self.balance = balance

	def deposit(self,amt):
		self.balance = self.balance + self.amt

		print('balance after deposit ',self.balance)

	def withdrawl(self,amt):
		if amt>self.balance:
			print('insufficient funds')
			sys.exit()
		self.balance = self.balance - amt
		print('balance after withdrawl = ',self.balance)

print('welcome to ', Customer.bankname)
name = input('enter the name = ')
c = Customer(name)

while True:
	print('d - deposit \nw - withdrawl \ne - exit')
	option = input('choose your option')
	if (option == 'd' or option == 'D'):
		amt = float(input('enter amount = '))
		c.deposit(amt)
	elif (option == 'w' or option == 'W'):
		amt = float(input('enter amount = '))
		c.withdrawl(amt)
	elif (option == 'e' or option == 'E'):
		print('thanks for banking')
		sys.exit()
	else:
		print('invalid option ...plz choose valid option')

