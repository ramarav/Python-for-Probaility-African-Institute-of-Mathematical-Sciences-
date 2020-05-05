#Q. No. 1:
#1. Suppose you have a fair six-sided die. Now suppose that you throw the die three times. What is the
#probability that you will get:
#(a) a 1 on the first throw, a 2 on the second throw, and a 3 on the third throw?
#(b) a 1, a 2, and a 3 in any order?
#(c) three sixes?

#Answer :
#(a)
#Generally, the probability of obtaining 1 on first through is 1/6 as there are 6 possibilities.
#Similarly, the possibility of obtaining 2 on second through and 3 on third through is also 1/3 each.
#If P(A) =P(B) = P(C) = 1/6
#Then, the total probability P =  P(A) * P(B) * P(C) = 1/6 ³
#The python code is shown below :
success = 0
tries = 0
for first in range (0,6) :
    for second in range (0,6) :
        for third in range (0,6):
            if first == 1 and second == 2 and third == 3:
                success+=1
            tries+=1
print (float(success)/tries)

#Answer = 0.004629629629629629 i.e. 1/6^3

