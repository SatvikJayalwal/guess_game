import os
os.system("cls")
import random
number = random.randrange(1,100)
tries_count = 0
guess = int(float(input("GUESS A NUMBER FROM 1 TO 100 : ")))
tries_count += 1
while (guess != number) :
    if guess < number :
       print(" YOUR NUMBER IS SMALLER THAN THE RANDOM NUMBER ")
       guess = int(float(input(" GUESS A NUMBER FROM 1 TO 100 : ")))
       tries_count += 1
    else :
       print(" YOUR NUMBER IS BIGGER THAN THE RANDOM NUMBER ")
       guess = int(float(input(" GUESS A NUMBER FROM 1 TO 100 : ")))
       tries_count += 1
print (" YOU HAVE GUESSED THE WRITE NUMBER ")
print (" NUMBER OF TRIES : " , tries_count)


    

































