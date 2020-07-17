#  Q. Write a program to find smallest of given 2 numbers?

a = 3
b = 1

if a<b:
	print('min is ',a)
else:
	print('min is ',b)


#  Q. Write a program to find smallest of given 3 numbers?

a = 23
b = 2
c =11

if a<b:
	if a<c:
		print('min is ',a)
	else:
		print('min is ',c)
else:
	if b<c:
		print('min is ',b)
	else:
		print('min is ',c)