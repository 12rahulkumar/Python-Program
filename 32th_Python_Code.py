# loops with else blocks

cart = [10,20,30,40,50]

for itr in cart:
	if itr>=500:
		print('we cannot process this order')
		break
	print(itr)
else:
	print('we can process all the order')

# ----------------------------------------------------------------------

cart = [10,20,500,600,30]

for itr in cart:
	if itr>=500:
		print('we cannot process this order')
		break
	print(itr)
else:
	print('we can process all the order')