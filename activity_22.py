#Modules -- Python file Management

import random

print("GUESSING GAME ....")

#setting up random values
random_value = random.randint(1,100)#generate random value (start, stop)
tries = 0
tuloy = True

while tuloy == True:
    num = eval(input("Guess a random number from 1 to 10 -->"))
    
    tries += 1
    if num == random_value:
        print("WINNER, send GCASH")
        print(f"random value is {random_value}")
        break
        
    else:
        print("Incorrect, Try again")
        continue
print(f"You guessed {tries} times") 
