string1 = "ABCdef"

#Concatination -> +
sum_string1 = string1 + string1[0]
print(string1) #output ABCdefA

#Indexing
print(string1[2]) 
print(string1[-3])

#Count Length
print(len(string1))

#String Comparison
print("Cdef" in string1)
string2 = "ABC"
print(string1 == string2)

#Q1
string_q1 = "ABCdef123"
print(string_q1 * 2) #--> ?

#Q2
string_q2 = "ABCdef135"
print(string_q2[9]) #--> ?


#empty list
list1 = []

#list with int values
list1 = [1, 2, 3]
print(list1)

#list with mixed int and string
list2 = ["aa", "bB", "CC", 4, 5, "CC"]
print(list2)

#Q3
list_q3 = ["abc", 34, True, 40, "male"]
list_q3 = [1, 2, 3]
print(list_q3) #--> ?

#Q4
#gimana yahhh caranya menggabungkan 2 list ini....? 🤔
list_a = ["abc", 34, True, 40, "male"]
list_b = [1, 2, 3]
list_q4 = list_a + list_b
print(list_q4)
#or
list_a.extend(list_b)
print(list_a)

#tuple
tuple1 = ("apple", "banana", "cherry", "apple")
print(type(tuple1))

#extend tuple
tuple2 = ("apple", "banana", "cherry", "apple")
addtuple = ("orange", 1, 2, 3)
tuple2 += addtuple
print(tuple2)
#or
tuple3 = tuple2 + addtuple
print(tuple3)