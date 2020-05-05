#(b)
#The answer to this problem is rather simple. Among the total combinations possible, half are odd and half are even (As the numbers are sequentially increasing). Hence, the answer is 1/2 = 0.5
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
