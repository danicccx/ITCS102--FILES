name = input("Input your name -->")
print("ODD NUMBER SUMMATION, press 0 to stop")
tuloy = True
sum = 0
odd = " "

while tuloy == True:
    num = eval(input("Input a random number --> "))
    
    if num % 2 == 1:
        print("ODD NUMBER DETECTED, code continues")
        sum += num
        odd += str(num) + " "
        continue
    elif num == 0:
         print("Program stops !!!")
         break
    else:
         print("Invalid input")
    continue
print(f"Hi {name}, the sum of all ODD number is {sum}")    
print(f"ODD numbers detected included the ff {odd}") 
