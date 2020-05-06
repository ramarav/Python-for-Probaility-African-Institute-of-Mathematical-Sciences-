
sum=0
n=0
tries=0
for first in range(1,7):
    for second in range(1,7):
        sum=int(first)+int(second)
        if sum%2 ==0 :
            n+=1
        tries+=1
print(int(n)/tries)
