#print("\t\t #", end = " ")

for blackforest in range(1,11,1):
    for takoyaki in range(10,blackforest,-1):
        print(" ", end = " ")
    for matcha in range(1,blackforest,1):
        print("#", end = " ")
    for rambutan in range(1,blackforest + 1, 1):
        print("#", end = " ")
    print( )
