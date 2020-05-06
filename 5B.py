
box1=0
box2=0
box3=0
tries1=0
tries2=0
tries3=0
for first in range(1,5):
    if first==1:
        box1+=1
    tries1+=1
a=float(box1)/tries1
for second in range(1,4):
    if second==1:
        box2+=1
    tries2+=1
b=float(box2)/tries2
for third in range(1,3):
    if third ==1:
        box3+=1
    tries3+=1
c=float(box3)/tries3
print('The probability of drawing the red ball from box u=1 is = ',float(a)/float(a+b+c))
print('The probability of drawing the red ball from box u=2 is = ',float(b)/float(a+b+c))
print('The probability of drawing the red ball from box u=3 is = ',float(c)/float(a+b+c))
