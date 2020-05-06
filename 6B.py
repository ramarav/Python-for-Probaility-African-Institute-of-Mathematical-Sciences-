s1=0
tries1=0
a=0
for first1 in range(1,7):
    if first1==1:
        continue
    for first2 in range(2,7):
        if first2==2:
            s1+=1
        tries1+=1
a+=1-float(s1)/tries1

s2=0
tries2=0
b=0
for second1 in range(3,7):
    if second1==3:
        continue
    for second2 in range(4,7):
        if second2==4:
            s2+=1
        tries2+=1
b+=1-float(s2)/tries2

s3=0
tries3=0
c=0
for third1 in range(5,7):
    if third1==1:
        continue
    for third2 in range(6,7):
        if third2==2:
            s3+=1
        tries3+=1
c+=1-s3/tries3
print('The probability = ',float(a*b*c)) 
