#  continue statement

# Eg 1: To print odd numbers in the range 0 to 9

for itr in range(10):
	if itr%2==0:
		continue
	print(itr)

cart = [10,20,500,700,50,60]

# ---------------------------------------------------------------

for itr in cart:
	if itr>=500:
		print('we cannot process this item ',itr)
		continue
	print(itr)

#  -----------------------------------------------------------------

numbers = [10,20,0,5,0,30]

for itr in numbers:
	if itr == 0:
		print('hey how we can divide the number by zero')
		continue
	print('100/{}={}'.format(itr,100/itr))	