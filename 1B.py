# (b)
#a 1, a 2, and a 3 in any order?
#Answer :
#The number of possibilities of getting 1, 2 and 3 in any order are :
#123
#132
#213
#231
#312
#321
#Hence, there are 6 possibilities.
#But the total possibilities are 111 to 666. i. e. 6^3
#Therefore, the total probability is 6/6^3 = 1/6^2
#The python code for this problem is shown below :
success = 0
tries = 0
for first in range(0,6):
    for second in range(0,6):
        for third in range(0,6):
            if first == 1 :
                if second == 2 :
                    if third == 3:
                        success+=1
                elif second == 3:
                    if third == 2 :
                        success+=1
            elif first == 2 :
                if second == 1 :
                    if third == 3:
                        success+=1
                elif second == 3:
                    if third == 1 :
                        success+=1
            elif first == 3 :
                if second == 1 :
                    if third == 2:
                        success+=1
                elif second == 2:
                    if third == 1 :
                        success+=1                               
            tries+=1
print (float(success)/tries)
#Ans : 0.027777777777777776 i.e. 6/6^3 = 1/6^2
