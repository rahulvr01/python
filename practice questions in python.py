n=int(input("Enter any number"))
a=len(str(n))
old=n
rev=0
Sumdigit=0
for i in range (100,2001,1):
    while n!=0:
        dig_which_we_access=n%10
        Sumdigit=Sumdigit+(dig_which_we_access**a)
        n=n//10
if old==Sumdigit:
    print("It's Armstrong")
else:
    print("not a armstrong number")

n=5
n=int(input("enter any number"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print (chr(65+j),end=" ")
    for j in range(i):
        print (chr(65+j),end=" ")
    print()

Sumdigit=0
for i in range(100,2001):
        dig=n%10
        Sumdigit=Sumdigit+(dig**a)
        n=n//10
    while n!=0:
    
for i in range:
if old==Sumdigit:
    print("It's Armstrong")
else:
    print("not a armstrong number")


for i in range (100,2001):
    a=len(str(i))
    old=i
    Sumdigit=0
    while i!=0:
        dig=i%10
        Sumdigit=Sumdigit+(dig**a)
        i=i//10
    if old==Sumdigit:
        print(Sumdigit)