#List Functions

myFave = ['Matcha', 'IceCream', 'Hotwheels', 'Blackforest', 'Mango']
print(myFave)

#every list has an index value/ address)
print(myFave[2])
print(myFave[2 : 5])

#adding an item to the end
myFave.append('Blue')
print(myFave)

#inserts item at a specified index
myFave.insert(3, 'Kali')
print(myFave)

#removes first occurence of item
myFave.remove('Mango')
print(myFave)

#removes and returns item at index
myFave.pop( )
print(myFave)

#returns number of elements
print(len(myFave))

#sorts the list (ascending by default)
myFave.sort( )
print(myFave)

#reverses the list order
myFave.reverse( )
print(myFave)
