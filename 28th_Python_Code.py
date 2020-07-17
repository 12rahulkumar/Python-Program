#  Q. Write a program to dispaly *'s in Right angled triangled form

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * * 
n = 7

for i in range(1,n+1):
	for j in range(1,i+1):
		print("*",end=" ")
	print()
