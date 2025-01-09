# zip function iterate equal 
l=[10,20,30,40,50]
l1=[100,200,300,400,500]
for i,j in zip(l,l1):
    print(i,j)

l=[10,20,30,40,50,60,70,80]
l1=[100,200,300,400,500]
for i,j in zip(l,l1):
    print(i,j)

l1=[5,1,2,4,3]
l2=[2,3,4,3,1]
# output [25,1,16,64,3]
l=[]
for i,j in zip(l1,l2):
    l.append(i**j)
print(l)

l1=[5,1,2,4,3]
l2=[2,3,4,3,1]
# output [25,1,16,64,3]
l=[]
for i,j in zip(l1,l2):
    l.append(i**j)
    print(l)l1=[5,1,2,4,3]
l2=[2,3,4,3,1]
# output [25,1,16,64,3]
l=[]
for i,j in zip(l1,l2):
    l.append(i**j)
    print(l)

l1=[5,1,2,4,3]
l2=[2,3,4,3,1]
# output [25,1,16,64,3]
l=[]
for i,j in zip(l1,l2):
    l.append(i**j)
print(l)

# list comprehension 
# syntax - [expression control flow function]
print([(i**j) for i,j in zip(l1,l2)])

# output 
# [1,8,27,64,125]
l=[]
for i in range(1,6):
    l.append(i**3)
print(l)
l1=([i**3 for i in range(1,6)])
print(l1)

l=[1,2,3,4,5,6,7,8,9,10]
# output - [1,3,5,7,9]
l1=[]
for i in range(1,11,2):
    print(i,end=",")

	