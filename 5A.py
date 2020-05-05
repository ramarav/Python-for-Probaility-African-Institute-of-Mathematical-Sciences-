# Q. No. 5 :
#Box u = 1 contains 1 red ball and 3 black balls. Box u = 2 contains 1 red ball, 1 white ball, and 1 black ball. Box u = 3 contains 1 red ball and 1 black ball.
#(a) A box is chosen at random and one ball is drawn. What is the probability that the ball is red?
#(b) Given that the ball is red, what are the probabilities that the chosen box was box u = 1, 2, 3?
#Answer : 
#(a) A box is chosen at random and one ball is drawn. What is the probability that the ball is red?
#There are 3 boxes.
#The probability of choosing any one box is 1/3.

#There are 4 balls in box u=1.
#Among these 4 balls 1 ball is red.
#The probability of drawing a red ball from box u=1 is 1/4.
#Among all the 3 boxes, the probability of drawing a red ball from this box is :
#P(A) =1/4*1/3 = 1/12.

#There are 3 balls in box u=2.
#Among these 3 balls 1 ball is red.
#The probability of drawing a red ball from box u=1 is 1/3.
#Among all the 3 boxes, the probability of drawing a red ball from this box is :
#P(B) =1/3*1/3 = 1/9.

#There are 2 balls in box u=3.
#Among these 2 balls 1 ball is red.
#The probability of drawing a red ball from box u=1 is 1/2.
#Among all the 3 boxes, the probability of drawing a red ball from this box is :
#P(C) =1/2*1/3 = 1/6.

#Now the total probability P = P(A)+P(B)+P(C)
#i. e. P = 1/12+1/9+1/6 = 13/36
#The python code for the solution of the above problem is given below :

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


