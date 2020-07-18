# display only even number

n = [1,2,3,4,5,6,7,8,9]

for itr in n:
	if itr%2 == 0:
		print(itr)

l=["A","B","C"]
x=len(l)
for i in range(x):
	print(l[i],"is available at positive index: ",i,"and at negative index: ",i-x) 
