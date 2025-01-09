#w a p p that determines the type of triangles based on the length of it three sides.
#types scalene , invalid , equilateral , isoleses
s1=int(input("enter the sides"))
s2=int(input("enter the sides"))
s3=int(input("enter the sides"))
if(s1+s2>s3 and s1+s3>s2 and s2+s3>s1):
    if (s1==s2==s3):
          print("equivalence triangle")
    elif(s1!=s2!=s3):
        print("scalene triangle")
    else:
        print("isoleses triangle")
else:
    print("invalid triangle")

year=int(input("enter the year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year, "leap year")
        else:
            print(year, "not a leap year")
    else:
        print(year,"leap year")
else:
    print(year, "not a leap year")


year=int(input("enter the year"))
if (year%4==0 and year%100!=0 or year%400==0):
    print("a leap year")
else:
    print("not a leap year")
