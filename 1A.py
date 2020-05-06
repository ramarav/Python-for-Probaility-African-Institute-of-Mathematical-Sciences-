
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

