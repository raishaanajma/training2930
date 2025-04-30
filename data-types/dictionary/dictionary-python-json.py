import json

myfamily = {
  "child1" : {
    "name" : "Emil",
    "birthday" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "birthday" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "birthday" : 2011
  }
}

print(myfamily["child1"])

with open("python-json.json", "w") as f:
    json.dump(myfamily, f, indent=4)