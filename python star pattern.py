n=int(input("enter a number"))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

n=int(input("enter a number"))
for i in range(n):
    for j in range(i-n,n-1):
        print("*",end=" ")
    print()

n=int(input("enter a number"))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

n=5
for i in range(n):
    for j in range(n-i-1):
        print("",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

n=5
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()

n=5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()

n=5
for i in range(n):
    for j in range(i):
        print("",end=" ")
    for j in range(n+1):
        print("*",end=" ")
    print()

n=5
for i in range(n):
    for j in range(n):
        print("",end=" ")
    for j in range(n):
        print("*",end=" ")
    print()

n=5
for i in range(n):
    for j in range(n):
        print("",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()

n=5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    for j in range(n-i-1):
        print("*",end=" ")
    print()

n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(2*i+1):
        if j==0 or j==2*i or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

n=5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    for j in range(2*(n-i)-1):
        print("*",end=" ")
    print()

#homework hollow star square
n=5
for i in range(n):
    for j in range(n):
        print("",end=" ")
    for j in range(2*i-1):
        if j==0 or j==2*i-1 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

n=5
for i in range(n):
    for j in range(n):
        print("",end=" ")
    for j in range(n):
        print("*",end=" ")
    print()

    n=5
for i in range(n):
    for j in range(n):
        print("",end=" ")
    for j in range(n):
        print("*",end=" ")
    print()