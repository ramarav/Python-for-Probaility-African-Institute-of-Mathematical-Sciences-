tie1=0
attempt1=0
a=0
for rop1 in range(1,7):
    if rop1==1:
        continue
    for rop2 in range(1,6):
        if rop2==1:
            tie1+=1
        attempt1+=1
a+=float(tie1)/attempt1

tie2=0
attempt2=0
b=0
for rop3 in range(1,5):
    if rop3==1:
        continue
    for rop4 in range(1,4):
        if rop4==1:
            tie2+=1
        attempt2+=1
b+=float(tie2)/attempt2

tie3=0
attempt3=0
c=0
for rop5 in range(1,3):
    if rop5==1:
        continue
    for rop6 in range(1,2):
        if rop6==1:
            tie3+=1
        attempt3+=1
c+=float(tie3)/attempt3

print('The probability = ',float(a*b*c))

