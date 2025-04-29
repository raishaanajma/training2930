#tuple
tuple1 = ("apple", "banana", "cherry", "apple")
print(type(tuple1))

#extend tuple
tuple2 = ("apple", "banana", "cherry", "apple")

tuple2[2] = "3" #expected error -immutable

addtuple = ("orange", 1, 2, 3)

tuple2 += addtuple

print(tuple2)

#or

tuple3 = tuple2 + addtuple
print(tuple3)