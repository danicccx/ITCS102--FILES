print("Welcome to Midnight’s Manga Recommender")
print ( )
print("Let me know your prefer genre:")
print("1. Tragedy")
print("2. Romance")
print("3. Action")
print( )
choice_genre = input("Enter choice (1/2/3): ")

if choice_genre == "1":
    print("Try 'Your Lie in April' ")
elif choice_genre == "2":
    print(" 'Kaguya-sama:Love is war' is our top recommendation")
elif choice_genre == "3":
    print(" 'Attack on Titan' is popular today")
else:
    print("Invalid genre, Please try again later.")
print( )

print("Let us proceed to your preferred decade!")
print( )
print("Which decade would you like? (2000s/2010s): ")
choice_decade = input("Please Enter your chosen decade: ")
if choice_decade == "2000s":
 print("We recommend 'Death Note' Manga")
elif choice_decade == "2010s":
    print("We recommend 'One Punch Man' Manga")

else:
 print("Opps! no recommendation for that")
print ( )
 
duration = input("Would you like a Manga with long duration? (yes/no):")

if duration == "yes":
         print( "We recommend 'One piece' with 300+ Chapters")
elif duration == "no":
             print(" 'The Promised Neverland' has 181 chapters only.")

else:
                 print("Sorry, We don’t have any recommendation")
print( )
 
print("We also have Manga recommendation from other genre (Comedy/Rom-Com/Children/Adventure/Fantasy): ")
others = input("Please enter the other genre that you like: ")

if others == "Comedy":
    print(" 'Great Teacher Onizuka' is our recommendation")
elif others == "Rom-com":
    print(" 'Horimiya' is our recommendation")
elif others == "Children":
    print(" 'Doraemon' is our recommnedation")
elif others == "Adventure":
    print(" 'Hunter x Hunter' is our recommemdation")
elif others == "Fantasy":
    print(" 'Berserk by Kentaro Miura' is our recommendation")

else:
    print("Invalid genre")
    print( )

print("A suitable Manga for you is here~")
age = eval(input("Enter your age to have a suitable recommendation: " ))
print( )

if age <= 0:
     print("No recommendation for your age")
elif age <= 5:
     print("No recommendation for your age ")
elif age <= 15:
    print(" We recommend 'Pokémon Adventures' ")
elif age >= 18:
    print(" We recommend 'Monster' ")

else:
    print("Invalid number")
print( )
 
print("Great! New Manga will be release soon. ")
new = 'Okay'
new = input(" Enter 'Okay' to stay updated for upcoming Mangas:")

if new == "Okay":
                 print(" 'Captain Underpants will be releason on April 7, 2026' ")
                 print(" 'Lone Wolf & Cub Deluxe Edition' is set for December 2025")
                 print( )
                 print("Thank you for using Midnigts’s Manga Recommender! Come Again Next Time.")
                 
else:
                 print("Thank you for using Midnight’s Manga Recommender!")
