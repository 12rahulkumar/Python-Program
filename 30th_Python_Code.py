#  break statement

for itr in range(10):
	if itr == 7:
		print('processing is enough , please break')
		break
	print(itr)


cart = [10,20,600,60,70]

for itr in cart:
	if itr>500:
		print('To place this order insurence must be required')
		break
	print(itr)