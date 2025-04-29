set1 = {"apple", "banana", "cherry"}

for x in set1:
  print(x)

set1.add("orange")
print(set1)

#remove/discard
set1.discard("orange")
print(set1)

#concat
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)