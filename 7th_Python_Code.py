# string data type

s1 = 'rahul'
s2 = "singh"
s3 = "'kumar"
s4 = 'a'

print(type(s1))
print(type(s2))
print(type(s3))
print(type(s4))

#  By using single quotes or double quotes we cannot represent multi line string literals.

#print("rahul kumar
#		singh")


#  For this requirement we should go for triple single quotes(''') or triple double quotes(""")

print("""rahul kumar
		singh""")

# index can be +ve or -ve
# +ve index --->  left to right
#  -ve index  --->  right to left

a = "rahul"
print(a[0])
print(a[1])
print(a[2])
print(a[-1])
print(a[-2])
print(a[-3])

#  print(a[45])  index out of range


print(a[1:40])
print(a[1:])
print(a[:4])
print(a[:])

print(a*2)
print(len(a))