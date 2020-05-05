#Answer :
#(b) Given that the ball is red, what are the probabilities that the chosen box was box u = 1, 2, 3?

#We know that box u=1 contains 4 balls among which 1 is a red ball.
#The probability of drawing a red ball here is P(A)=1/4.

#Similarly box u=2 contains 3 balls among which 1 is a red ball.
#The probability of drawing a red ball here is P(B)=1/3.

#And box u=3 contains 2 balls among which 1 is a red ball.
#The probability of drawing a red ball here is P(C)=1/2.


#The red ball might have been drawn from box u=1 OR u=2 OR u=3.
#OR indicates addition.
#Hence total probability is P=P(A)+P(B)+P(C)=1/4+1/3+1/2 = 13/12

#Now the probability of drawing a red ball from box u=1 is P(A)/P = 3/13.
#The probability of drawing a red ball from box u=2 is P(B)/P = 4/13.
#The probability of drawing a red ball from box u=3 is P(C)/P = 6/13
#The python code is given below :
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
