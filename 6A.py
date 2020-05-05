#Q. No. 6 :
#Three identical skipping ropes are dropped in a heap. The six free ends of the ropes are picked up by three people—each person picks up one free end with his right hand and another free end with his left. Then they all step away from each other.
#(a) What is the probability that every person finds he is holding a single skipping rope?
#(b) What is the probability that the three people are joined in a single closed chain?
#Answer :
#(a) What is the probability that every person finds he is holding a single skipping rope?
#There are 3 ropes.
#Each rope has two ends.
#Therefore, there are a total of 6 ends.
#Let us call the rope ends as follows :


#Rope                               Ends
#  1                                   1 – 2
#  2                                   3 – 4
#  3                                   5 - 6

#Let us assume that the first person catches rope 1- end 1.
#Now he has got 5 more ends left.
#The probability of getting end 2 is therefore P(A) = 1/5

#Let us now assume that the second person catches rope 2- end 3.
#Now he has got 3 more ends left.
#The probability of getting end 4 is therefore P(B) = 1/3

#Let us assume that the third person catches rope 3- end 5.
#Now he has got only 1 more end left.
#The probability of getting end 6 is therefore P(C) = 1/1= 1

#Therefore the total probability is P = P(A)*P(B)*P(C)= 1/5*1/3*1=1/15

#The python code for the same is given below :


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

