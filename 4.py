# Q. No. 4 :
#What is the probability of drawing an ace or a heart from a pack of 52 playing cards?
#Answer :
#We know that the total number of playing cards are 52.
#Among these, there are four types.

 #   Spades
 #   Diamonds
 #   Hearts
 #   Clubs

#Hence, the number of heart cards are 13 (52/4).
#The number of aces (A's) are four...Among which one is of hearts.
#Hence, there are three aces which are not hearts.
#Our problem is to draw either a heart card or an ace. Hence, we have to draw any one of these 16 (13+3) cards from total 52 cards.
#Therefore the probability is P=16/52.
#The python code solution for this problem is given below :
s=0
tries=0
for prob in range(1,53):
    if prob < 17:
        s+=1
    tries+=1
print (float(s)/tries)
##Ans:
##>>>
##0.3076923076923077
##>>> s
##16
##>>> tries
##52
##>>>
