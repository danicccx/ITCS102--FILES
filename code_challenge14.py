print("List of Favorite Anime Titles")
anime_list = [ ]
print("Type 'done' when you are finished. \n")

while True:
    anime = input("Enter the Anime title (or 'done' to stop):")
    
    if anime.lower ( ) == 'done':
        break
       
    anime_list.append(anime)
    print(f" {anime} added to your list!\n")
 
print("\n Your Anime List")  
for title in anime_list:
    print(f"- {title}")
