# (c)
#The probability of getting a six on first or second or third die is 1/6
#The total probability is the sum of all these probabilities.
#If P(A) =P(B) = P(C) = 1/6
#Then, the total probability P = P(A) * P(B) * P(C) = 1/6 ³
#The python code is shown below :
success = 0
tries = 0
for first in range(1,7):
    for second in range(1,7):
        for third in range(1,7):
            if first == 6 and second == 6 :
                if third == 6 :
                    success+=1
            tries+=1
print ('Success=',success)
print ('tries=',tries)
print ('Probability=',float(success)/tries)
#Ans = 0.004629629629629629 i.e. 1/6^3 
