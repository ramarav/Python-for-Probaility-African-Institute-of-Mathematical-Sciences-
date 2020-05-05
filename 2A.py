# Q. No. 2 :
#Two dice are rolled. We define s as the sum of the values on the two faces. 
#(a) What is the mean (expected value) of s? 
#(b) What is the probability that s is even? 
#Answer :
#(a) 
#Mean is the average value. 
#Each die can have a value 1 to 6. 
#Hence the sum can be 2 to 12.
#11
#12
#13
#14
#15
#16
#21
#22
#23
#24
#25
#.... 
#....
#....
#64
#65
#66
#Hence there are 36 possible combinations.
#The total sum can be 252.
#Hence the mean is 252/36 = 7

#The python code is given below :

n = 0
sum=0
for first in range(1,7):
    for second in range(1,7):
        sum+=int(first)+int(second)
        n+=1
print (int(sum)/n) 


