set1 = {"orange", "banana", "cherry"}

for rehan in set1:
  print(rehan)

set1.add("apple")
print(set1)
print(len(set1))

#remove/discard
set1.discard("orange")
print(set1)

#concat
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)