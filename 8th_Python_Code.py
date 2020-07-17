#  type conversion
#  it means we can convert one type of value to another type

# 1.int()  ==>>  We can use this function to convert values from other types to int

print(int(123.45))
print(int('12'))

#  print(int(2+3j))  error
print(int(True))

#  print(int('10.5')) error
#  print(int('ten'))  error
#  print(int('0b1111'))  error


#2. float()  ==>>  We can use float() function to convert other type values to float type.


print(float(10))

#print(float(2+3j)) error

print(float(True))
print(float('10'))
print(float('10.5'))


# 3.complex()  ==>>  We can use this function to convert x into complex number with real part x and imaginary part 0

print(complex(10))
print(complex(10.5))
print(complex(True))
print(complex(False))
print(complex("10"))
print(complex("10.5"))

# print(complex("ten"))  error

print(complex(10,-2))


#  4.bool()  ==>> We can use this function to convert other type values to bool type.

print(bool(0))
print(bool(1))
print(bool(10))
print(bool(10.5))
print(bool(0.178))
print(bool(0.0))
print(bool(10-2j))
print(bool(0+1.5j))
print(bool(0+0j))
print(bool("True"))
print(bool("False"))
print(bool("")) 


# 5.str()  ==>>  We can use this method to convert other type values to str type
print(str(10))
print(str(10.5))
print(str(10+2j))
print(str(True))