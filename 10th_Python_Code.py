# byte data type  range -> 0 to 256

#  bytes data type represens a group of byte numbers just like an array.

x = [10,20,30,40]

print(type(x))

b = bytes(x)

print(type(b))

print(b[0])
print(b[-1])

for itr in b:
	print(itr)

#  Once we creates bytes data type value, we cannot change its values,otherwise we will get 

#   b [0] = 100   error

#----------------------------------------------------------------------------------------------------------------------

# bytearray data type
# bytearray is exactly same as bytes data type except that its elements can be modified.

x = [1,2,3,4]
print(type(x))

b = bytearray(x)
print(type(b))

for itr in b:
	print(itr)

b[0] = 100
b[-1] = 200

for itr in b:
	print(itr)	

# bytearray range must be in between (0,256)