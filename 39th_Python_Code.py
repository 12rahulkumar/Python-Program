# Q. Write a program to access each character of string in forward and backward direction by using while loop?

name = "rahul kumar singh"
n = len(name)
print(n)
i = 0

while i<n:
	print(name[i],end=" ")
	i = i+1

print()

i = -1

while i>=-n:
	print(name[i],end=" ")
	i = i-1 

print()

for itr in name:
	print(itr,end=" ")

print()

for itr in name[::-1]:
	print(itr,end=" ")