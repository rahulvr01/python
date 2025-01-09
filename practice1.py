m=int(input("enter any number"))
s=int(input("enter any number"))
l=int(input("enter any number"))
avg=(m+s+l)
if avg>=85 and m>=70 and s>=70 and l>=70:
    print("eligible for honors")
elif m<50 or s<50 or l<50:
    print("remedial classes")
else:
    print("standard placement")
    

a_s=int(input("enter any number"))
m_s=int(input("enter any number"))
f_s=int(input("enter any number"))
att=int(input("enter any number"))
w_a_s=a_s*0.3
w_m_s=m_s*0.3
w_f_s=f_s*0.3
w_att=att*0.1
total_marks=w_a_s+w_m_s+w_f_s+w_att
if att>=95:
    total_marks=total_marks+5
if total_marks>90:
    print("A")
elif total_marks>=80:
    print("B")
elif total_marks>=70:
    print("C")
elif total_marks>=60:
    print("D"):


