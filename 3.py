
s=0
tries=0
for first in range(1,7):
    for second in range(1,7):
        for third in range(1,7):
            for fourth in range(1,7):
                for fifth in range(1,7):
                    if first==6:
                        s+=1
                    elif second==6:
                        s+=1
                    elif third==6:
                        s+=1
                    elif fourth==6:
                        s+=1
                    elif fifth==6:
                        s+=1
                    tries+=1
print(float(s)/tries)
#Ans : 0.5981224279835391
#>>> tries
#7776
#>>> s
#4651 
