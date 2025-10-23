isMadumi = True
sum = 0
while isMadumi == True:
    confirm = input("Do you wish to continue washing (yes ? no)").lower()
    sum += 1
    
    if confirm == 'yes':
        print("Washing continues...")
        continue
    else:
        print("Washing stops...")
        break

print("Number of cycle is", sum)
