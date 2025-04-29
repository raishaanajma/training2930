dictionary1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#access value
dictionary1["brand"]
print(dictionary1["brand"])

#list of keys
dictionary1.keys()
print(dictionary1.keys())

#add new pair
dictionary1["color"] = "white"
print(dictionary1)

#remove
dictionary1.pop("year")
print(dictionary1)
#or
del dictionary1["brand"]
print(dictionary1)

#delete entire