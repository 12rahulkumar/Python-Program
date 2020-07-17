# id operators

a = 10
b = 10 
print(a is b)

c = 10.6
d = 10.6
print(c is d)

e = 2+3j
f = 2+3j
print(e is f)

x = True
y = True
print(x is y)


a="durga"
b="durga"
print(id(a))
print(id(b))
print(a is b) 


list1=["one","two","three"]
list2=["one","two","three"]
print(id(list1))
print(id(list2))
print(list1 is list2) 
print(list1 is not list2)
print(list1 == list2)


# membership operators

# We can use Membership operators to check whether the given object present in the given collection.(It may be String,List,Set,Tuple or Dict)

list1=["sunny","bunny","chinny","pinny"]
print("sunny" in list1) 
print("tunny" in list1) 
print("tunny" not in list1) 

x="hello learning Python is very easy!!!"
print('h' in x) 
print('d' in x) 
print('d' not in x) 
print('Python' in x) 