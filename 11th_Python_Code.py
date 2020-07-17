# lsit data type

list = [1,2,3,4,"rahul",10.6,True]
list.append("singh")
list.remove(2)
list[0] = 100

print(list)
print(type(list))


# tuple data type = it is the read only version of list

# no append , no remove , no update

list1 = (1,2,3,5,5,"rahul")

print(type(list1))
print(list1)


# range data type
# range Data Type represents a sequence of numbers.
# not modified , no =assignment

print(range(10))

r = range(10)
for itr in r:
	print(itr,end = " ")

print('\n')
for itr in range(10,20):
	print(itr,end=" ")

print('\n')	
for itr in range(10,20,2):
	print(itr,end="")

print('\n')

# l = list(range(10))
# print(l)


# set data type
# If we want to represent a group of values without duplicates where order is not important then we should go for set Data Type.
# no index checking , no duplicates


s = {1,2,3,4,"rahul"}
# print(s[0])  error 
s.add("singh")
s.remove('rahul')
print(s)

# frozenset data type 
# It is exactly same as set except that it is immutable.

s = {10,20,30,40}
fs = frozenset(s)

print(type(fs))



# dict data type
# If we want to represent a group of values as key-value pairs then we should go for dict 
# Duplicate keys are not allowed but values can be duplicated.
 # If we are trying to insert an entry with duplicate key then old value will be replaced with new value.

d = {101:'durga',102:'ravi',103:'singh'}
d[101]='sunny'
d['a'] = "apple"
print(d)