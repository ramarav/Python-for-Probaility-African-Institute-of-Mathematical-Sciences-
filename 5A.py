
s1=0
tries1=0
s2=0
tries2=0
s3=0
tries3=0
for box in range(1,4):
    for ball in range(1,5):
        if box==1:
            if ball==1:
                s1+=1
        tries1+=1
    for ball in range(1,4):
        if box==2:
            if ball==1:
                s2+=1
        tries2+=1
    for ball in range(1,3):
        if box ==3:
            if ball==1:
                s3+=1
        tries3+=1
print((float(s1)/tries1)+(float(s2)/tries2)+(float(s3)/tries3))
#0.36111111111111105
#>>> 13/36
#0.3611111111111111


