# complex data type

# complex = x + yj
# where x is real part and y is the imaginary part

a = 3+5j
print(a)

b = 10+5.5j
print(b)

c = 0.5+0.1j
print(c)

print(type(a))

#In the real part if we use int value then we can specify that either by decimal,octal,binary or hexa decimal form.

d = 0b11+12j
print(d)

# sum of 2 complex number
print('a + b = ',a+b)

# to access the real part
print('real part of a = ',a.real)

# to acces the imaginary part
print('imaginary part of a = ',a.imag)