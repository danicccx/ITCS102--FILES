temp = eval(input("Enter Temperature: --->"))

if temp <= 0:
    print("The Temperature is Below Freezing")
elif temp >= 1 and temp <= 15:
    print("The Temperature is Extremely Cold")
elif temp >= 16 and temp <= 30:
    print("Today, The Temperature is Cold")
elif temp >= 31 and temp <= 38:
    print("Today is only a Lukewarm Temperature")
elif temp >= 39 and temp <= 42:
    print("It is a Warm Temperature")
elif temp >= 43 and temp <= 50:
    print("Hot Temperatures")
elif temp >= 51 and temp <= 60:
    print("Extremely Hot Temperatures")
elif temp >= 61:
    print("Burning Temperatures")
  
else:
    print("Invalid Temperature")
