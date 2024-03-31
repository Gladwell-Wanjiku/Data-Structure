myTuple = ("Kenya","Tanzania","Sudan", "Malawi","Jamaica")
print(myTuple)
#changing a tuple into a list
myTuple2 = list(myTuple)
print(myTuple2)

#adding an element to the list
myTuple2.append("Nigeria")
print(myTuple2)

#changing tuple values
myTuple2[2]=("Ethiopia")
print(myTuple2)

#removing an item
myTuple2.remove("Malawi")
print(myTuple2)

#changing the list back to a tuple
myTuple3 = tuple(myTuple2)
print(myTuple3)

#length of the tuple
print(len(myTuple3))

#finding elements in the tuple
print(myTuple3[4])
print(myTuple3[-2])
print(myTuple3[2:4])
print(myTuple3[ :4])