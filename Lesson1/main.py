##Today I learned while loops if conditions inupts and random numbers.

import random
num = random.randrange (1,10)
i = 0 
while i < 3:
    l = int(input("Pick a number from 1-10 "))
    if l == num:
        print ("You Win!!!")
        break
    else:
        print ("Try again")   
    i=i+1

    if i == 3:
        print("Game over the number was ", num)
        
    


